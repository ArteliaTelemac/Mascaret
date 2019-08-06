# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Mascaret
Description          : Pre and Postprocessing for Mascaret for QGIS
Date                 : December,2017
copyright            : (C) 2017 by Artelia
email                :
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import math as m
import os

import numpy as np

class ClassLaws:
    """
    Class contain the different methods to create the laws
    """
    def __init__(self, parent):
        self.parent = parent
        self.mgis = self.parent.mgis
        self.mdb = self.parent.mdb
        self.tbst = self.parent.tbst
        self.grav = self.parent.grav
        self.dico_abc = {}
        self.dossier_file_masc = os.path.join(self.mgis.masplugPath, "mascaret")
        self.dico_name_abac = {}
        self.param_g = {}
        self.poly_p = None
        self.qh_j_no_hy = []
        # valeur pour éviter des débit null et blocker le model
        self.deb_min = 0.0001

    def init_method(self, id_config):
        """
        intialisation variables
        :param id_config:  index of hydraulic structure
        :return:
        """

        if self.parent.checkprofil(id_config):
            profil = self.parent.get_profil(id_config)
        else:
            msg = "Profile copy isn't found"
            self.mgis.add_info(msg)
            return

        list_recup = ['FIRSTWD', 'NBTRAVE',
                      'ZTOPTAB', 'COEFDS', 'COEFDO',
                      # numeric
                      'MAXH', 'MINH', 'PASH', 'PASQ']
        self.param_g = self.parent.get_param_g(list_recup, id_config)
        list_key = list(self.param_g.keys())
        if not 'COEFDO' in list_key:
            self.param_g['COEFDO'] = 1
        if not 'COEFDS' in list_key:
            self.param_g['COEFDS'] = 0.385

        self.param_g['NBPIL'] = self.param_g['NBTRAVE'] - 1
        self.poly_p = self.parent.poly_profil(profil)

        poly_tmp = self.parent.coup_poly_h(self.poly_p, self.param_g['ZTOPTAB'])
        (minx, miny, maxx, maxy) = poly_tmp.bounds
        self.param_g['TOTALW'] = maxx - minx

        (minx, miny, maxx, maxy) = self.poly_p.bounds
        self.minz = miny
        self.list_zav = list(
            np.arange(self.minz + self.param_g['MINH'], self.param_g['MAXH'] + self.minz, self.param_g['PASH']))
        self.list_zav.append(self.param_g['MAXH'] + self.minz)

        self.list_zam = np.array(self.list_zav)

        where = " id_config={} and type=0 ".format(id_config)
        order = "id_elem"
        self.list_poly_trav = self.parent.select_poly('struct_elem', where, order)['polygon']

        self.param_elem = {'ZMAXELEM': [], 'LARGELEM': [], 'SURFELEM': [], 'ZMINELEM': []}

        for poly in self.list_poly_trav:
            (minx, miny, maxx, maxy) = poly.bounds
            self.param_elem['ZMAXELEM'].append(maxy)
            self.param_elem['LARGELEM'].append(maxx - minx)
            self.param_elem['SURFELEM'].append(poly.area)
            self.param_elem['ZMINELEM'].append(miny)

    def check_listinter(self, dico_abc, name_abc, varx, vary):
        """
        Check the interpolated list
        :param dico_abc: dico where the lists are contained
        :param name_abc: key of dico
        :param varx: key of x value
        :param vary: key of y value
        :return: new list
        """
        if len(dico_abc[name_abc][varx]) == len(dico_abc[name_abc][vary]):
            return dico_abc[name_abc][varx], dico_abc[name_abc][vary]
        else:
            list_inter_x = []
            list_inter_y = []
            for idx, orderx in enumerate(dico_abc[name_abc]['order_{}'.format(varx)]):
                for jdx, ordery in enumerate(dico_abc[name_abc]['order_{}'.format(vary)]):
                    if orderx == ordery:
                        list_inter_x.append(dico_abc[name_abc][varx][idx])
                        list_inter_y.append(dico_abc[name_abc][vary][jdx])
            return list_inter_x, list_inter_y

    def check_coefm(self, coefm, verb=False):
        """
        Check m coeficient to test  application domain
        :param coefm: m coeficient
        :param verb: verb: verbose yes or no
        :return:
        """
        cond = True
        msg = 'The following coeficients leave application domain :\n'
        if coefm < 0.45:
            msg += '\t - Kp coeficient\n'
            cond = False
        if coefm < 0.3:
            msg += '\t - Kb coeficient\n'
            cond = False
        if coefm < 0.2 or coefm > 1:
            msg += '\t - Ke coeficient\n'
            cond = False
        if coefm < 0.3 or coefm > 1:
            msg += '\t - Ks coeficient\n'
            cond = False
        if m.isnan(coefm):
            msg = '\t m coeficient is NAN\n'
            cond = False
        if not cond and verb:
            print(msg)
        return cond

    def check_j(self, j, form, q, h, verb=False):
        """
        Check j parameter and modifie
        :param j: parameter method Bradley
        :param form: Span form
        :param q: flow rate
        :param h: water level
        :param verb: verbose yes or no
        :return:
        """
        msg = 'The j coeficients > {} for {} span form with q = {} and h = {}.\n'
        cond = True
        if form == 1 and j > 0.057:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 2 and j > 0.067:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 3 and j > 0.095:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 4 and j > 0.116:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 5 and j > 0.14:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 6 and j > 0.166:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 7 and j > 0.18:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
        if form == 8 and j > 0.18:
            if [q, h] not in self.qh_j_no_hy:
                cond = False
                self.qh_j_no_hy.append([q, h])
            j = 0.18  # hyp for working
        if verb and not cond:
            print(msg.format(j, form, q, h))
        return j

    def init_bradley(self, method, id_config):
        """
        initialisation for bradley method
        :param method: mehtod of compute
        :param id_config:  index of hydraulic structure
        :return:
        """
        list_recup = ['BIAIOUV',
                      'FORMCUL', 'ORIENTM',
                      'PENTTAL', 'EPAITAB', 'BIAICUL',
                      # pile de pont
                      'LARGPIL', 'LONGPIL', 'FORMPIL', 'BIAIPIL',
                      # numeric
                      'MAXQ', 'MINQ']
        param_g_temp = self.parent.get_param_g(list_recup, id_config)
        self.param_g.update(param_g_temp)
        self.param_g['BIAIOUV'] = self.param_g['BIAIOUV'] / 180. * m.pi  # rad
        # only brad
        where = " id_config={} and type=1 ".format(id_config)
        order = "id_elem"
        self.list_poly_pil = self.parent.select_poly('struct_elem', where, order)['polygon']

        self.list_q = list(np.arange(self.param_g['MINQ'], self.param_g['MAXQ'], self.param_g['PASQ']))
        self.list_q.append(self.param_g['MAXQ'])

        self.dico_name_abac = {
            'Bradley 78': {'abac': ['bradley', 'bradley78']},
            'Bradley 72': {'abac': ['bradley', 'bradley72']}
        }
        self.dico_abc = self.parent.get_abac(self.dico_name_abac[method]['abac'])
        self.param_g['TOTALOUV'] = 0
        for poly in self.list_poly_trav:
            (minx, miny, maxx, maxy) = poly.bounds
            self.param_g['TOTALOUV'] += (maxx - minx)

        self.type_kb = self.def_type_kb(method)

        if self.param_g['BIAICUL'] == '0':
            self.abac_dks = "dKs_casA_abac"
        else:
            self.abac_dks = "dKs_casB_abac"

        self.list_ph = []
        for key in self.dico_abc[self.abac_dks].keys():
            if key != 'M' and key != 'phi>45' and 'order_' not in key:
                self.list_ph.append((key, float(key.split('=')[1])))
        self.list_ph = sorted(self.list_ph)

        self.list_e = []
        for key in self.dico_abc['dKe_abac'].keys():
            if key != 'M' and 'order_' not in key:
                self.list_e.append((key, float(key.split('=')[1])))
        self.list_e = sorted(self.list_e)

        self.coef_cor_biais = (self.param_g['LONGPIL'] * m.sin(self.param_g['BIAIOUV']) +
                               self.param_g['LARGPIL'] * m.cos(self.param_g['BIAIOUV'])) / self.param_g['LARGPIL']

    def meth_brad(self, zav, q, coef_cor_biais, type_kb, list_ph, list_e):
        """
        Compute  h upstream with bradley method
        :param zav: zav cote downstream
        :param q: flow rate
        :param coef_cor_biais: angle correction coefficient
        :param type_kb: kb coefficient type
        :param list_ph: phi list in abacus
        :param list_e: e list in abacus
        :return  [flowrate, h downstream, h upstream]
        """

        area_pil = 0
        area_pil_proj = 0

        poly_wet = self.parent.coup_poly_h(self.poly_p, zav)
        if poly_wet.is_empty:
            return None
        area_wet = poly_wet.area
        # print('area_wet',area_wet)
        umoy = q / area_wet
        for poly_pil in self.list_poly_pil:
            poly_pil = self.parent.coup_poly_h(poly_pil, zav)
            if self.param_g['BIAIOUV'] != 0:
                area_pil_proj += poly_pil.area * coef_cor_biais
            area_pil += poly_pil.area
        if area_pil_proj == 0:
            area_pil_proj = area_pil
        left_bank = self.param_g['FIRSTWD'] + self.param_g['TOTALOUV'] + self.param_g['LARGPIL'] * len(
            self.list_poly_pil)
        ssoh = self.parent.coup_poly_v(poly_wet, [self.param_g['FIRSTWD'], left_bank],
                                       typ='LR').area
        q1 = ssoh * umoy
        q2 = self.parent.coup_poly_v(poly_wet, self.param_g['FIRSTWD'], typ='R').area * umoy
        q3 = self.parent.coup_poly_v(poly_wet, left_bank, typ='L').area * umoy
        qtot = q1 + q2 + q3
        alpha1 = 1
        alpha2 = 1
        if qtot != 0:
            coefm = q1 / qtot
        else:
            # hyp si debit null cote aval =cote amon
            # list_final.append([q, zav, zav])
            return [self.deb_min, zav, zav]
            # coefm = 0

        # print('q1,q2,q3',q1,q2,q3)
        # print('area q1, area q2,area q3', ssoh,
        # self.parent.coup_poly_v(poly_wet,self.param_g['FIRSTWD'],typ='R').area,
        #       self.parent.coup_poly_v(poly_wet,left_bank,typ='L' ).area)
        # print(self.param_g['FIRSTWD'],left_bank)
        # print('coefm', coefm)
        if not self.check_coefm(coefm):
            return None

        s1 = ssoh - area_pil_proj
        # print('S1',s1)
        va = q / s1
        # print('Va', va)
        # *************** kb
        list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, "kb_abac", 'M', type_kb)
        kb = np.interp(coefm, list_inter_x, list_inter_y)

        # *************** Dkp
        # print(area_pil_proj,ssoh,area_pil)
        j = area_pil_proj / ssoh
        j = self.check_j(j, int(self.param_g['FORMPIL']), q, zav)
        # print('j',j)
        list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, 'DKp_abac', 'J',
                                                          str(int(self.param_g['FORMPIL'])))
        dkp = np.interp(j, list_inter_x, list_inter_y)

        # print('Dkp', dkp)
        list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, 's_abac', 'M',
                                                          str(int(self.param_g['FORMPIL'])))
        coefs = np.interp(coefm, list_inter_x, list_inter_y)
        # print('s', coefs)
        dkp = dkp * coefs
        # print('sDkp',dkp)
        if q3 < q2:
            e_calc = 1 - q3 / q2
        elif q2 < q3:
            e_calc = 1 - q2 / q3
        else:
            e_calc = 0

        list_m_interp = []
        list_e_interp = []
        for ee in list_e:
            list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, 'dKe_abac', 'M', ee[0])
            inter_tmp = np.interp(coefm, list_inter_x, list_inter_y)
            list_m_interp.append(inter_tmp)
            list_e_interp.append(ee[1])

        dke = np.interp(e_calc, list_e_interp, list_m_interp)
        # print('dke', dke)

        if self.param_g['BIAIPIL'] == 0:
            dks = 0
        else:
            if self.param_g['BIAIOUV'] > 45:
                list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, self.abac_dks, 'M', 'phi>45')
                dksx = np.interp(coefm, list_inter_x, list_inter_y)
            else:

                list_m_interp = []
                list_ph_interp = []
                for ph in list_ph:
                    list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, self.abac_dks, 'M', ph[0])
                    inter_tmp = np.interp(coefm, list_inter_x, list_inter_y)
                    list_m_interp.append(inter_tmp)
                    list_ph_interp.append(ph[1])
                dksx = np.interp(self.param_g['BIAIOUV'], list_ph_interp, list_m_interp)

            if dksx > 0:
                dks = dksx
            else:
                dks = 0
        # print("dks",dks)
        term1 = (kb + dkp + dke + dks) * va ** 2 / (2. * self.grav) * alpha2
        # print("term1 Remout",term1)
        hmon = zav + term1
        poly_wet = self.parent.coup_poly_h(self.poly_p, hmon)
        area_amont = poly_wet.area
        term2 = alpha1 * ((s1 / area_wet) ** 2 - (s1 / area_amont) ** 2) * va ** 2 / (
            2. * self.grav)
        # print("term2 Remout", term2)
        remout = term1 + term2

        # print("Remous Total", remout)
        return [q, zav, zav + remout]

    def filtre_list(self, liste, val_g, val_d):
        """
        To filter list
        :param liste: list to filter
        :param val_g: left value
        :param val_d:  right value
        :return: (list)
        """
        idx = np.where(val_g < liste)[0]
        sortie = liste[idx]
        idx = np.where(sortie < val_d)[0]

        return list(sortie[idx])

    def bradley(self, id_config, method='Bradley 78', ui=None):
        """
        Bradley method for structure
        :param id_config:  index of hydraulic structure
        :param method: mehtod of compute
        :param ui: gui object
        :return: law list
        """
        self.init_method(id_config)
        list_final = []

        self.init_bradley(method, id_config)

        val = 75 / len(self.list_zav)

        # self.list_zav=[9.75,6.25]
        ztransi = min(self.param_elem['ZMAXELEM'])

        for zav in self.list_zav:
            list_final = self.calc_law_brad(list_final, zav, ztransi)
            if ui is not None:
                ui.progress_bar(val)
        # correction of the law
        list_final = self.transition_charge(list_final, ztransi)
        list_final = self.complete_law(list_final)
        if ui is not None:
            ui.progress_bar(90)
        self.save_list_final(list_final, id_config, method)
        if ui is not None:
            ui.progress_bar(100)
        self.write_csv(list_final)

        return list_final

    def calc_law_brad(self, list_final, zav, ztransi):
        """
        Compute bradley method
        :param list_final: list of law values
        :param zav: z dowstream
        :param ztransi: z transition stream (free surface flow and flow under load)
        :return: new list of law values
        """
        list_brad = []
        brad_lim = None
        for q in self.list_q:
            value = self.meth_brad(zav, q, self.coef_cor_biais,
                                   self.type_kb, self.list_ph, self.list_e)
            # [q, zav, zav + remout]
            if value is None:
                continue
            else:
                if value[2] > ztransi:
                    brad_lim = value
                    break
                list_brad.append(value)

        # treatment transition law
        list_ori = []
        if len(list_brad) > 0:
            qmax = max(np.array(list_brad)[:, 0])
            if qmax <= self.param_g['MAXQ']:
                return list_final + list_brad
            # interpol ztrans
            list_ori.append(list_brad[-1])
            if brad_lim:
                # interpolation
                q_tmp = np.array([list_brad[-1][0], brad_lim[0]])
                zam_tmp = np.array([list_brad[-1][2], brad_lim[2]])
                q_new = np.interp(ztransi, zam_tmp, q_tmp)
                list_ori = list_ori + [[q_new, zav, ztransi]]
                # list_final += [[q_new ,zav ,ztransi]]
                qmax = q_new
                za = ztransi
            else:
                qmax = max(np.array(list_brad)[:, 0])
                za = list_brad[-1][2]
        else:
            qmax = self.deb_min
            za = zav
            list_ori.append([qmax, zav, za])

        idx = np.where(self.list_zam > za)[0]
        if len(idx) > 0:
            zcret = self.param_g['ZTOPTAB']
            for zam in self.list_zam[idx[0]:]:
                if zav != zam:
                    q_seuil = 0
                    q_ori = 0
                    for i, zsup in enumerate(self.param_elem['ZMAXELEM']):

                        q_ori += self.meth_orif(zam, zav, self.param_elem['ZMINELEM'][i], zsup, zcret,
                                                self.param_elem['LARGELEM'][i], self.param_g['COEFDS'],
                                                self.param_g['COEFDO'], self.param_elem['SURFELEM'][i])

                    # print('zam q_ori',zam, q_ori)
                    if zam >= zcret:
                        q_seuil = self.meth_seuil(zam, zav, zcret, self.param_g['COEFDS'], self.param_g['TOTALW'])
                    # print('q_seuil',zam, q_seuil)
                    if q_ori == 0 and q_seuil == 0:
                        value = None
                    else:
                        value = [q_ori + q_seuil, zav, zam]
                    if value is None:
                        continue
                    else:
                        if value[0] > self.param_g['MAXQ']:
                            list_ori.append(value)
                            break
                        list_ori.append(value)

        # interpol q fix
        if len(list_ori) > 1:
            idx = np.where(np.array(self.list_q) > list_ori[0][0])[0]
            if len(idx) > 0:
                list_q_tmp = self.list_q[idx[0]:]
            else:
                list_q_tmp = self.list_q
            q_tmp = np.array(list_ori)[:, 0]
            zam_tmp = np.array(list_ori)[:, 2]
            zam_f = np.interp(list_q_tmp, q_tmp, zam_tmp)
            interpol_list = [[a, b, c] for a, b, c in zip(list_q_tmp, [zav] * len(zam_f), zam_f)]
            list_ori = interpol_list
        else:
            list_ori = []

        return list_final + list_brad + list_ori

    def transition_charge(self, list_final, ztransi):
        """
        Treatment of transition flow (free surface flow and flow under load)
        :param list_final: list of law values
        :param ztransi:  z transition stream
        :return: new list of law values
        """
        list_add = []
        if isinstance(ztransi, list):
            uniques = np.unique(np.array(ztransi))
            for z_tmp in uniques:
                list_add += self.calc_transi(list_final, z_tmp)
        else:
            list_add = self.calc_transi(list_final, ztransi)
        list_final = list_final + list_add
        return list_final

    def calc_transi(self, list_final, ztransi):
        """
        Compute value of transition flow (free surface flow and flow under load)
        :param list_final: list of law values
        :param ztransi:  z transition stream
        :return: added value list
        """
        list_add = []

        info = self.parent.sort_law(list_final)
        # add Z pour  acroite le point d'infexion
        for id, deb in enumerate(self.list_q):
            # cherche nb de debi
            idxq = np.where(info[:, 0] == deb)[0]
            # cherche position transition

            idxz = np.where(info[idxq, 2] < ztransi)[0]
            # if deb==100:
            #     print(info[idxq, 1],idxz)
            if len(idxz) > 0:
                idxz = idxq[0] + idxz[-1]
                tab_tmp = info[idxz, :]
                tab_tmp1 = info[idxz + 1, :]
                # print(tab_tmp, tab_tmp1, deb)
                # print(tab_tmp[1],tab_tmp1[1])
                zmoy = (tab_tmp[1] + tab_tmp1[1]) / 2
                ecartmoy = (tab_tmp1[2] + tab_tmp[2]) / 2 - zmoy
                ecart1 = tab_tmp[2] - tab_tmp[1]
                ecart2 = tab_tmp1[2] - tab_tmp1[1]
                # print(ecart1, ecart2,ecartmoy,'*****', deb)
                if ecart2 < ecartmoy:
                    ecart2 = ecartmoy
                if ecart1 > ecartmoy:
                    ecart1 = ecartmoy

                z1 = (tab_tmp[1] + 2 * zmoy) / 3
                z2 = (tab_tmp1[1] + 2 * zmoy) / 3

                list_add.append([deb, z1, z1 + ecart1])
                list_add.append([deb, zmoy, (tab_tmp1[2] + tab_tmp[2]) / 2])
                list_add.append([deb, z2, z2 + ecart2])

        return list_add

    def delete_doublon(self, liste):
        """
        Delete  duplicate value
        :param liste: list
        :return: new list
        """
        data = np.array(liste)
        sorted_idx = np.lexsort(data.T)
        sorted_data = data[sorted_idx, :]

        # Get unique row mask
        row_mask = np.append([True], np.any(np.diff(sorted_data, axis=0), 1))
        # Get unique rows
        out = sorted_data[row_mask]
        return list(out)

    def complete_law(self, list_final):
        """
        Add value to have the same value number for q and z downstream
        :param list_final: list of law values
        :return: new_list: new list of law values
        """
        info = self.parent.sort_law(list_final)
        unique, counts = np.unique(info[:, 1], return_counts=True)
        nb_val = max(counts)
        list_val = []
        new_list = []
        for val, cpt in zip(unique, counts):
            if cpt != nb_val:
                list_val.append(val)
        for id, deb in enumerate(self.list_q):
            idxq = np.where(info[:, 0] == deb)[0]
            tab = info[idxq, :]
            modif = False
            add_val = []
            for val in list_val:
                if not (val in tab[:, 1]):
                    modif = True
                    zam_f = np.interp(val, tab[:, 1], tab[:, 2])
                    add_val.append([deb, val, zam_f])
            if modif:
                new_list = new_list + list(tab) + add_val
            else:
                new_list += list(tab)

        new_list= self.delete_doublon(new_list)

        return new_list

    def save_list_final(self, list_final, id_config, method):
        """
        Save in database the law value
        :param list_final: list of law values
        :param id_config:  index of hydraulic structure
        :param method: mehtod of compute
        :return: nothing
        """
        # **********************************************************************************************
        # save
        # *********************************************************************************************
        if list_final == []:
            sql = "SELECT name FROM {0}.{1} WHERE id={2}".format(self.mdb.SCHEMA, 'struct_config', id_config)

            name = self.mdb.run_query(sql, fetch=True)
            name = name[0][0]

            sql = "UPDATE {0}.{1} SET {2}  WHERE id={3};".format(self.mdb.SCHEMA, 'struct_config', 'active=False',
                                                                 id_config)
            self.mdb.run_query(sql)

            self.mgis.add_info(
                "No values for the law because the coefficients leave application domain of the method.\n"
                "The <<{}>> hydraulic structur is deactivated".format(name))
        else:
            self.parent.save_law_st(method, id_config, list_final)

    def def_type_kb(self, method):
        """
        Compute kb coeficient
        :param method: compute method
        :return:
        """
        if method == 'Bradley 78':
            if self.param_g['TOTALOUV'] > 60 and self.param_g['FORMCUL'] == 1:
                type_kb = 'Others'
            else:
                type_kb = 'type1<60m'
                list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, "kb_abac", 'M', type_kb)
                self.dico_abc["kb_abac"]['M'] = list_inter_x
                self.dico_abc["kb_abac"][type_kb] = list_inter_y

        elif method == 'Bradley 72':
            if self.param_g['FORMCUL'] == 1:
                type_kb = 'type1'
            elif self.param_g['FORMCUL'] == 2:
                if self.param_g['ORIENTM'] == 30:
                    type_kb = 'type2_30deg'
                else:
                    type_kb = 'type2_45to60deg'
            elif self.param_g['FORMCUL'] == 3:
                if self.param_g['PENTTAL'] == 0:
                    type_kb = 'type3_1:1'
                elif self.param_g['PENTTAL'] == 1:
                    type_kb = 'type3_1.5:1'
                else:
                    type_kb = 'type3_2:1'
            else:
                # defaut 1
                type_kb = 'type1'
                # list_inter_x, list_inter_y = self.check_listinter(self.dico_abc, "kb_abac", 'M', type_kb)
        return type_kb

    def meth_seuil(self, zam, zav, zcret, cf, larg):
        """
        Compute threshold law
        :param zam: z upstream
        :param zav: z downstream
        :param zcret: z crest
        :param larg: wide
        :param cf: flow rate coeficient for threshold law
        :return: q : flow rate
        """
        ct = cf * m.sqrt(2 * self.grav)
        typ_s = 0  # 0 :'thick', 1: thin

        h1 = max(zam - zcret, 0)
        h2 = max(zav - zcret, 0)
        if h1 == 0 and h2 == 0:
            return 0
        ham = max(h1, h2)
        hav = min(h1, h2)
        r = hav / ham
        if h1 >= h2:
            sens_ecoul = 1
        else:
            sens_ecoul = -1

        q_denoy = ct * larg * m.pow(ham, 1.5)

        if typ_s == 0:
            if r <= 0.8:
                k = 1
            elif 0.8 < r <= 1:
                k = -25 * m.pow(r, 2) + 40 * r - 15
            else:
                k = 0
        else:
            if ham == 0.:
                k = 1
            else:
                k = m.pow(m.pow(1 - r, 1.5), 0.385)
        q = sens_ecoul * k * q_denoy

        return q

    def meth_orif(self, zam, zav, zinf, zsup, zcret, larg, cf, cfo, surf):
        """
        Compute orifice law
        :param zam: z upstream
        :param zav: z downstream
        :param zinf: z orifice bottom
        :param zsup: z orifice top
        :param zcret: z crest
        :param larg: wide
        :param cf: flow rate coeficient for threshold law
        :param cfo: flow rate coeficient for orifice law
        :param surf: wet area of orifice
        :return: q : flow rate
        """
        ouv = zsup - zinf
        h1 = zam - zinf
        h2 = zav - zinf
        hav = min(h1, h2)
        ham = max(h1, h2)
        epsd = 0.01
        epso = 0  # 0.05 * (zcret - zsup)
        rac_epsd = m.sqrt(0.01)
        ct = cfo * m.sqrt(2 * self.grav)
        if h1 >= h2:
            sens_ecoul = 1
        else:
            sens_ecoul = -1
        if ham < 0:
            print('erreur loi orifice ham <0')
            return None

        if surf < 0.:
            return 0
        qo = 0
        qs = 0
        if ham < ouv + epso:  # working threshold

            qs = self.meth_seuil(zam, zav, zinf, cf, larg)

        if ham > ouv:  # working orifice
            a2 = 0.65
            # a1 = ouv / ham
            # a2 = 0.65
            # # if 0.55<= a1 < 0.9 :
            #         a2 = 0.5 + 0.268 * a1
            # elif 0.9<= a1 :
            #         a2 = 0.745 + 2.55 * (a1 - 0.9)
            if (ham - hav) <= epsd:  # linear treatment for the little gap
                qo = surf * a2 * (ham - hav) / rac_epsd

            else:
                a3 = max(hav, 0.5 * ouv)
                qo = surf * a2 * m.sqrt(ham - a3)
        qo = ct * qo
        if ham < ouv:
            q = qs
        elif ham >= ouv + epso:
            q = qo
        else:
            q = qs + (ham - ouv) * (qo - qs) / epso
        q = sens_ecoul * q

        return q

    def search_qmax(self, tmp):
        """
        search the most little max
        :param tmp: list of values
        :return: max
        """
        list_qmax = []
        for zav in np.unique(tmp[:, 1]):
            idx = np.where(tmp[:, 1] == zav)[0]
            if len(idx) > 0:
                list_qmax.append(max(tmp[idx, 0]))
        if list_qmax:
            qmax = min(list_qmax)
        else:
            qmax = max(tmp[:, 0])

        return qmax

    def interpol_list_final_for_new_q(self, list_final, pasq=10, list_q=None):
        """
        Search the  new (q, zav) couple and interpole with new q
        :param list_final: list of law values
        :param pasq q discretisation
        :return: list_final: new list of law values
        :return: q_new: q list of law
        """

        tmp = np.array(list_final)
        if list_q != None:
            q_new=list_q
        else:
            qmin = min(tmp[:, 0])
            qmax = max(tmp[:, 0])
            # int(qmin) for around value
            q_new = np.arange(int(qmin), qmax, pasq)
            q_new[0] = qmin
        list_final = []
        for zav in np.unique(tmp[:, 1]):
            idx = np.where(tmp[:, 1] == zav)[0]
            if len(idx) > 1:
                q_tmp = tmp[idx, 0]
                zam_tmp = tmp[idx, 2]
                zam_f = np.interp(q_new, q_tmp, zam_tmp)
                interpol_list = [[a, b, c] for a, b, c in zip(q_new, [zav] * len(zam_f), zam_f)]
                list_ori = interpol_list
            else:
                list_ori = []
            list_final = list_final + list_ori

        return list_final, q_new



    def find_zam_dicho(self, min_elem, idx_min, q, zav):
        """ find zam with weir law"""
        largmin = 0.1  # largeur mini pour buse circulaire valeur arbitraire
        epsi_zam = 0.1  # ajout pour le calcul de la largeur buse circulaire  0.1 arbitrair
        prec = 1E-4  # precision dichotomie

        ct = self.param_g['COEFDS'] * m.sqrt(2 * self.grav)
        debut = min_elem
        fin = self.list_zav[-1]
        ecart = fin - debut

        while ecart > prec:
            zam_tmp = (debut + fin) / 2
            qnew = 0
            for poly in self.list_poly_trav:
                (minx, miny, maxx, maxy) = poly.bounds
                z_elem = miny
                larg = maxx - minx
                # cas buse circulaire ?
                # cas ou dalot n'a pas une largeur régulière ?

                # poly_wet = self.parent.coup_poly_h(poly, zam_tmp)
                # if poly_wet.is_empty:
                #     larg = largmin
                # else:
                #     (minx, miny, maxx, maxy) = poly.bounds
                #     larg = maxx - minx
                qnew += self.meth_seuil(zam_tmp, zav, z_elem, self.param_g['COEFDS'], larg)
            # print('zam,qnew',zam_tmp,qnew)
            if qnew > q:
                fin = zam_tmp
            else:
                debut = zam_tmp
            ecart = fin - debut
        return zam_tmp



    def calc_law_borda(self, list_final, zav, zcret, ztr, min_elem):
        """
        Compute the law with borda method + threshold law
        :param list_final: list of law values
        :param zav: z dowstream
        :param zcret: z Crest
        :param ztr: z transition stream (threshold)
        :return: list_final: new list of law values
        """
        list_borda = []
        borda_lim = None
        print("******", zav)


        idx_min=self.param_elem['ZMINELEM'].index(min_elem)
        ct = self.param_g['COEFDS']* m.sqrt(2 * self.grav)
        cond_zmin = False
        pr_area_wet = self.area_wet_fct(self.poly_p, zav)
        pr_area_wet_cret = self.area_wet_fct(self.poly_p, ztr)

        area_wet = 0
        for poly_trav in self.list_poly_trav:
            area_wet += self.area_wet_fct(poly_trav, zav)

        for q in self.list_q :

            if zav <= min_elem:
                cond_zmin = True
                zam = self.find_zam_dicho(min_elem,idx_min,q,zav)
            else:
                zam = self.find_zam_dicho(min_elem, idx_min, q, zav)
                # 0.25 limitant si coef  borda trop petit (le rapport surface ouvrage et aval superieur à 4)
                # 2/3 limitant si coef de borda 1
                if zav / zam > 2 / 3. and area_wet / pr_area_wet > 0.25:
                    zam = self.meth_borda_z(pr_area_wet, area_wet, q, zav)
                    cond_zmin =False
                else:
                    cond_zmin = True

            # [q, zav, zam]
            if zam > ztr:
                borda_lim = [q, zav, zam]
                break
            list_borda.append([q, zav, zam])

        list_ori = []
        if len(list_borda) > 0:
            qmax = max(np.array(list_borda)[:, 0])
            if qmax >= self.param_g['MAXQ'] or cond_zmin :
                 return list_final + list_borda
            # interpol ztrans
            list_ori.append(list_borda[-1])
            if borda_lim:
                # interpolation
                q_tmp = np.array([list_borda[-1][0], borda_lim[0]])
                zam_tmp = np.array([list_borda[-1][2], borda_lim[2]])
                q_new = np.interp(zcret, zam_tmp, q_tmp)
                list_ori = list_ori + [[q_new, zav, ztr]]
                qmax = q_new
                za = zcret
            else:
                qmax = max(np.array(list_borda)[:, 0])
                za = list_borda[-1][2]
        else:
            qmax = self.deb_min
            za = zav
            list_ori.append([qmax, zav, za])

        idx = np.where(self.list_zam > za)[0]
        if len(idx) > 0:

            for zam in self.list_zam[idx[0]:]:
                if zav != zam:
                    q_seuil = 0
                    q_ori = self.meth_borda_q(pr_area_wet_cret, area_wet, zam, zav)
                    # print('zam q_ori',zam, q_ori)
                    if zam >= zcret:
                        q_seuil = self.meth_seuil(zam, zav, zcret, self.param_g['COEFDS'], self.param_g['TOTALW'])
                    # print('q_seuil',zam, q_seuil)
                    if q_ori == 0 and q_seuil == 0:
                        value = None
                    else:
                        value = [q_ori + q_seuil, zav, zam]
                    if value is None:
                        continue
                    else:
                        if value[0] > self.param_g['MAXQ']:
                            list_ori.append(value)
                            break
                        list_ori.append(value)
        # interpol q fix
        if len(list_ori) > 1:
            idx = np.where(np.array(self.list_q) > list_ori[0][0])[0]
            if len(idx) > 0:
                list_q_tmp = self.list_q[idx[0]:]
            else:
                list_q_tmp = self.list_q
            q_tmp = np.array(list_ori)[:, 0]
            zam_tmp = np.array(list_ori)[:, 2]
            zam_f = np.interp(list_q_tmp, q_tmp, zam_tmp)
            interpol_list = [[a, b, c] for a, b, c in zip(list_q_tmp, [zav] * len(zam_f), zam_f)]
            list_ori = interpol_list
        else:
            list_ori = []
        return list_final + list_borda + list_ori

    def borda(self, id_config, method='Borda', ui=None):
        """
        Borda method for structure
        :param id_config:  index of hydraulic structure
        :param method: mehtod of compute
        :param ui: gui object
        :return: law list
        """
        self.init_method(id_config)

        list_recup = ['MAXQ', 'MINQ', 'COEFBOR']
        param_g_temp = self.parent.get_param_g(list_recup, id_config)
        self.param_g.update(param_g_temp)
        self.list_q = list(np.arange(self.param_g['MINQ'], self.param_g['MAXQ'], self.param_g['PASQ']))
        self.list_q.append(self.param_g['MAXQ'])

        list_final = []
        zcret = self.param_g['ZTOPTAB']
        val = 75 / len(self.list_zav)
        area_tot = 0.
        for poly_trav in self.list_poly_trav:
            area_tot += poly_trav.area

        min_elem = min(self.param_elem['ZMINELEM'])
        for zav in self.list_zav:
            list_final = self.calc_law_borda(list_final, zav, zcret, zcret, min_elem)


            if list_final is None:
                self.mgis.add_info("Problem : creation law")

            if ui is not None:
                ui.progress_bar(val)


        # list_final, self.list_q = self.interpol_list_final_for_new_q(list_final, pasq=self.param_g['PASQ'],
        #                                                              list_q=self.list_q)
        # self.write_csv(list_final, name =r'mascaret\av_law.csv' )
        list_final = self.transition_charge(list_final,zcret)
        list_final = self.complete_law(list_final)

        if ui is not None:
            ui.progress_bar(90)

        if self.mgis.DEBUG:
            self.write_csv(list_final)

        self.save_list_final(list_final, id_config, method)
        if ui is not None:
            ui.progress_bar(100)
        return list_final

    def write_csv(self, list_final,name=r"mascaret\law_tmp.csv"):
        """
        Write CSV to check law
        :param list_final:
        :return:
        """

        f = open(os.path.join(self.mgis.masplugPath, name), 'w')
        f.write('q ;zav ;zam \n')
        for val in list_final:
            f.write('{}; {} ;{} \n'.format(val[0], val[1], val[2]))
        f.close()

    def orifice(self, id_config, method='Loi d\'orifice', ui=None):
        """
        Orifice method for structure
        :param id_config:  index of hydraulic structure
        :param method: mehtod of compute
        :param ui: gui object
        :return: law list
        """

        self.init_method(id_config)
        list_final = []
        qmax = self.deb_min  # self.param_g['MINQ']
        zcret = self.param_g['ZTOPTAB']
        val = 90 / len(self.list_zav)
        first_trans = True
        ztransi = []
        largmin=0.1 # buse circulaire
        for zav in self.list_zav:

            idx = np.where(self.list_zam > zav)[0]
            if len(idx) > 0:
                # debut debit mini attention traitemen peut être différent
                if self.list_zam[idx[0] - 1] == zav:
                    value = [self.deb_min, zav, self.list_zam[idx[0] - 1]]
                    list_final.append(value)

                for zam in self.list_zam[idx[0]:]:
                    q_seuil = 0
                    q_ori = 0

                    for i, zsup in enumerate(self.param_elem['ZMAXELEM']):
                        if first_trans:
                            ztransi.append(zsup)

                        val=self.meth_orif(zam, zav, self.param_elem['ZMINELEM'][i], zsup, zcret,
                                                self.param_elem['LARGELEM'][i], self.param_g['COEFDS'],
                                                self.param_g['COEFDO'], self.param_elem['SURFELEM'][i])
                        if val != None:
                            q_ori += val

                    first_trans = False
                    if zam >= zcret:
                        q_seuil = self.meth_seuil(zam, zav, zcret, self.param_g['COEFDS'], self.param_g['TOTALW'])
                        # print('q_seuil', q_seuil,zav,zam)
                    if q_ori is None:
                        value = None
                    else:
                        value = [q_ori + q_seuil, zav, zam]
                    if value is None:
                        continue
                    else:
                        if value[0] > qmax:  # and value[0] > qtest:
                            # print('ori va',value)
                            list_final.append(value)
                            # # impose debit toujours superieur
                            # qtest = value[0]
                        else:
                            value = [qmax, zav, zam]
                            list_final.append(value)
            if ui is not None:
                ui.progress_bar(val)
        # treament of law for Mascaret model
        list_final, self.list_q = self.interpol_list_final_for_new_q(list_final, pasq=self.param_g['PASQ'])
        list_final = self.transition_charge(list_final, ztransi)
        list_final = self.complete_law(list_final)
        if self.mgis.DEBUG:
            self.write_csv(list_final)
        self.save_list_final(list_final, id_config, method)
        if ui is not None:
            ui.progress_bar(100)
        return list_final

    def meth_borda_q(self, sav, sc, zam, zav):
        """
        Compute z upstream with borda method
        :param sav: wet surface dowstream
        :param sc:  wet surface at the hydraulic structure
        :param zam: z upstream
        :param zav: z dowstream
        :return: q: flow rate
        """
        k = (sav / sc - 1) ** 2 + 1 / 9.
        q = m.sqrt((zam - zav) * 2 * self.grav / k) * sav * self.param_g['COEFBOR']
        return q

    def meth_borda_z(self, sav, sc, q, zav):
        """
        Compute z upstream with borda method
        :param sav: wet surface dowstream
        :param sc: wet surface at the hydraulic structure
        :param q: flow rate
        :param zav: z dowstream
        :return: zam: z upstream
        """
        k = (sav / sc - 1) ** 2 + 1 / 9.
        # print(k)
        # print((q / (sav * self.param_g['COEFBOR'])) ** 2)
        # print(sav,self.param_g['COEFBOR'])
        zam = (q / (sav * self.param_g['COEFBOR'])) ** 2 * k / (2 * self.grav) + zav
        return zam

    def area_wet_fct(self, poly, zw):
        """
        Compute wet surface
        :param poly: polygone
        :param zw: water level
        :return: wet surface
        """
        poly_wet = self.parent.coup_poly_h(poly, zw)
        if poly_wet.is_empty:
            return 0
        return poly_wet.area
