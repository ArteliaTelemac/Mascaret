# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_water_quality.ui'
#
# Created: Tue Jan 09 17:21:08 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Parameter_water_q(object):
    def setupUi(self, Parameter_water_q):
        Parameter_water_q.setObjectName(_fromUtf8("Parameter_water_q"))
        Parameter_water_q.resize(740, 608)
        self.gridLayout_2 = QtGui.QGridLayout(Parameter_water_q)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.WaterQ = QtGui.QTabWidget(Parameter_water_q)
        self.WaterQ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WaterQ.setObjectName(_fromUtf8("WaterQ"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.modeleQualiteEau = QtGui.QComboBox(self.tab)
        self.modeleQualiteEau.setObjectName(_fromUtf8("modeleQualiteEau"))
        self.modeleQualiteEau.addItem(_fromUtf8(""))
        self.modeleQualiteEau.addItem(_fromUtf8(""))
        self.modeleQualiteEau.addItem(_fromUtf8(""))
        self.modeleQualiteEau.addItem(_fromUtf8(""))
        self.modeleQualiteEau.addItem(_fromUtf8(""))
        self.modeleQualiteEau.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.modeleQualiteEau, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_modeleQualiteEau = QtGui.QLabel(self.tab)
        self.label_modeleQualiteEau.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_modeleQualiteEau.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_modeleQualiteEau.setObjectName(_fromUtf8("label_modeleQualiteEau"))
        self.gridLayout.addWidget(self.label_modeleQualiteEau, 1, 0, 1, 1)
        self.presenceTraceurs = QtGui.QCheckBox(self.tab)
        self.presenceTraceurs.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.presenceTraceurs.setObjectName(_fromUtf8("presenceTraceurs"))
        self.gridLayout.addWidget(self.presenceTraceurs, 0, 0, 1, 1)
        self.label_nbTraceur = QtGui.QLabel(self.tab)
        self.label_nbTraceur.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_nbTraceur.setObjectName(_fromUtf8("label_nbTraceur"))
        self.gridLayout.addWidget(self.label_nbTraceur, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.nbTraceur = QtGui.QSpinBox(self.tab)
        self.nbTraceur.setMinimum(1)
        self.nbTraceur.setMaximum(10)
        self.nbTraceur.setObjectName(_fromUtf8("nbTraceur"))
        self.gridLayout.addWidget(self.nbTraceur, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.b_add_lineTabTracer = QtGui.QPushButton(self.tab)
        self.b_add_lineTabTracer.setEnabled(True)
        self.b_add_lineTabTracer.setObjectName(_fromUtf8("b_add_lineTabTracer"))
        self.verticalLayout_5.addWidget(self.b_add_lineTabTracer)
        self.b_delete_lineTabTracer = QtGui.QPushButton(self.tab)
        self.b_delete_lineTabTracer.setEnabled(True)
        self.b_delete_lineTabTracer.setObjectName(_fromUtf8("b_delete_lineTabTracer"))
        self.verticalLayout_5.addWidget(self.b_delete_lineTabTracer)
        spacerItem4 = QtGui.QSpacerItem(20, 23, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.WaterQ.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.table_InitC = QtGui.QTableWidget(self.tab_2)
        self.table_InitC.setObjectName(_fromUtf8("table_InitC"))
        self.table_InitC.setColumnCount(3)
        self.table_InitC.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_InitC.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_InitC.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_InitC.setHorizontalHeaderItem(2, item)
        self.gridLayout_4.addWidget(self.table_InitC, 0, 1, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.b_add_line = QtGui.QPushButton(self.tab_2)
        self.b_add_line.setObjectName(_fromUtf8("b_add_line"))
        self.verticalLayout_3.addWidget(self.b_add_line)
        self.b_delete_line = QtGui.QPushButton(self.tab_2)
        self.b_delete_line.setObjectName(_fromUtf8("b_delete_line"))
        self.verticalLayout_3.addWidget(self.b_delete_line)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.WaterQ.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.optionCalculDiffusion_seo = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_seo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_seo.setObjectName(_fromUtf8("optionCalculDiffusion_seo"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_seo, 8, 1, 1, 1)
        self.optionCalculDiffusion_Fisher = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_Fisher.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_Fisher.setObjectName(_fromUtf8("optionCalculDiffusion_Fisher"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_Fisher, 4, 2, 1, 1)
        self.LimitPente = QtGui.QComboBox(self.tab_3)
        self.LimitPente.setEnabled(False)
        self.LimitPente.setObjectName(_fromUtf8("LimitPente"))
        self.LimitPente.addItem(_fromUtf8(""))
        self.LimitPente.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.LimitPente, 2, 1, 1, 1)
        self.optionCalculDiffusion_isawa = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_isawa.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_isawa.setObjectName(_fromUtf8("optionCalculDiffusion_isawa"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_isawa, 5, 2, 1, 1)
        self.label_frequenceCouplHydroTracer = QtGui.QLabel(self.tab_3)
        self.label_frequenceCouplHydroTracer.setObjectName(_fromUtf8("label_frequenceCouplHydroTracer"))
        self.gridLayout_5.addWidget(self.label_frequenceCouplHydroTracer, 0, 0, 1, 1)
        self.label_ordreSchemaConvec = QtGui.QLabel(self.tab_3)
        self.label_ordreSchemaConvec.setObjectName(_fromUtf8("label_ordreSchemaConvec"))
        self.gridLayout_5.addWidget(self.label_ordreSchemaConvec, 1, 2, 1, 1)
        self.ordreSchemaConvec = QtGui.QComboBox(self.tab_3)
        self.ordreSchemaConvec.setObjectName(_fromUtf8("ordreSchemaConvec"))
        self.ordreSchemaConvec.addItem(_fromUtf8(""))
        self.ordreSchemaConvec.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.ordreSchemaConvec, 1, 3, 1, 1)
        self.label_optionCalculDiffusion = QtGui.QLabel(self.tab_3)
        self.label_optionCalculDiffusion.setObjectName(_fromUtf8("label_optionCalculDiffusion"))
        self.gridLayout_5.addWidget(self.label_optionCalculDiffusion, 3, 0, 1, 1)
        self.frequenceCouplHydroTracer = QtGui.QSpinBox(self.tab_3)
        self.frequenceCouplHydroTracer.setMinimum(1)
        self.frequenceCouplHydroTracer.setMaximum(999999999)
        self.frequenceCouplHydroTracer.setProperty("value", 1)
        self.frequenceCouplHydroTracer.setObjectName(_fromUtf8("frequenceCouplHydroTracer"))
        self.gridLayout_5.addWidget(self.frequenceCouplHydroTracer, 0, 1, 1, 1)
        self.label_optionConvection = QtGui.QLabel(self.tab_3)
        self.label_optionConvection.setObjectName(_fromUtf8("label_optionConvection"))
        self.gridLayout_5.addWidget(self.label_optionConvection, 1, 0, 1, 1)
        self.optionConvection = QtGui.QComboBox(self.tab_3)
        self.optionConvection.setObjectName(_fromUtf8("optionConvection"))
        self.optionConvection.addItem(_fromUtf8(""))
        self.optionConvection.addItem(_fromUtf8(""))
        self.optionConvection.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.optionConvection, 1, 1, 1, 1)
        self.optionCalculDiffusion_default = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_default.setObjectName(_fromUtf8("optionCalculDiffusion_default"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_default, 3, 1, 1, 1)
        self.optionCalculDiffusion_liu = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_liu.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_liu.setObjectName(_fromUtf8("optionCalculDiffusion_liu"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_liu, 5, 1, 1, 1)
        self.optionCalculDiffusion_deng = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_deng.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_deng.setObjectName(_fromUtf8("optionCalculDiffusion_deng"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_deng, 8, 2, 1, 1)
        self.optionCalculDiffusion_keefer = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_keefer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_keefer.setObjectName(_fromUtf8("optionCalculDiffusion_keefer"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_keefer, 6, 1, 1, 1)
        self.label_LimitPente = QtGui.QLabel(self.tab_3)
        self.label_LimitPente.setEnabled(False)
        self.label_LimitPente.setObjectName(_fromUtf8("label_LimitPente"))
        self.gridLayout_5.addWidget(self.label_LimitPente, 2, 0, 1, 1)
        self.optionCalculDiffusion_Mirasol = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_Mirasol.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_Mirasol.setObjectName(_fromUtf8("optionCalculDiffusion_Mirasol"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_Mirasol, 7, 2, 1, 1)
        self.optionCalculDiffusion_elder = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_elder.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_elder.setObjectName(_fromUtf8("optionCalculDiffusion_elder"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_elder, 4, 1, 1, 1)
        self.optionCalculDiffusion_magazine = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_magazine.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_magazine.setObjectName(_fromUtf8("optionCalculDiffusion_magazine"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_magazine, 7, 1, 1, 1)
        self.paramW = QtGui.QDoubleSpinBox(self.tab_3)
        self.paramW.setEnabled(False)
        self.paramW.setDecimals(4)
        self.paramW.setMinimum(-1000000000.0)
        self.paramW.setMaximum(1000000000.0)
        self.paramW.setProperty("value", 0.0)
        self.paramW.setObjectName(_fromUtf8("paramW"))
        self.gridLayout_5.addWidget(self.paramW, 2, 3, 1, 1)
        self.label_paramW = QtGui.QLabel(self.tab_3)
        self.label_paramW.setEnabled(False)
        self.label_paramW.setObjectName(_fromUtf8("label_paramW"))
        self.gridLayout_5.addWidget(self.label_paramW, 2, 2, 1, 1)
        self.optionCalculDiffusion_falconer = QtGui.QRadioButton(self.tab_3)
        self.optionCalculDiffusion_falconer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionCalculDiffusion_falconer.setObjectName(_fromUtf8("optionCalculDiffusion_falconer"))
        self.gridLayout_5.addWidget(self.optionCalculDiffusion_falconer, 6, 2, 1, 1)
        self.coeffDiffusion_default = QtGui.QDoubleSpinBox(self.tab_3)
        self.coeffDiffusion_default.setEnabled(False)
        self.coeffDiffusion_default.setMinimum(-1000000000.0)
        self.coeffDiffusion_default.setMaximum(1000000000.0)
        self.coeffDiffusion_default.setObjectName(_fromUtf8("coeffDiffusion_default"))
        self.gridLayout_5.addWidget(self.coeffDiffusion_default, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.table_conv_diff = QtGui.QTableWidget(self.tab_3)
        self.table_conv_diff.setObjectName(_fromUtf8("table_conv_diff"))
        self.table_conv_diff.setColumnCount(3)
        self.table_conv_diff.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_conv_diff.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_conv_diff.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_conv_diff.setHorizontalHeaderItem(2, item)
        self.table_conv_diff.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.table_conv_diff)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.b_phy_param = QtGui.QPushButton(self.tab_3)
        self.b_phy_param.setObjectName(_fromUtf8("b_phy_param"))
        self.horizontalLayout_2.addWidget(self.b_phy_param)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.b_meteo_param = QtGui.QPushButton(self.tab_3)
        self.b_meteo_param.setObjectName(_fromUtf8("b_meteo_param"))
        self.horizontalLayout_2.addWidget(self.b_meteo_param)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.WaterQ.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.concentInit = QtGui.QCheckBox(self.tab_5)
        self.concentInit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.concentInit.setObjectName(_fromUtf8("concentInit"))
        self.verticalLayout.addWidget(self.concentInit)
        spacerItem10 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)
        self.loiTracer = QtGui.QCheckBox(self.tab_5)
        self.loiTracer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.loiTracer.setObjectName(_fromUtf8("loiTracer"))
        self.verticalLayout.addWidget(self.loiTracer)
        spacerItem11 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem11)
        self.concentrations = QtGui.QCheckBox(self.tab_5)
        self.concentrations.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.concentrations.setObjectName(_fromUtf8("concentrations"))
        self.verticalLayout.addWidget(self.concentrations)
        spacerItem12 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem12)
        self.bilanTracer = QtGui.QCheckBox(self.tab_5)
        self.bilanTracer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bilanTracer.setObjectName(_fromUtf8("bilanTracer"))
        self.verticalLayout.addWidget(self.bilanTracer)
        self.gridLayout_6.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 1, 2, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem14, 1, 0, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem15, 0, 1, 1, 1)
        self.WaterQ.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.WaterQ, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Parameter_water_q)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.actionB_add_line = QtGui.QAction(Parameter_water_q)
        self.actionB_add_line.setObjectName(_fromUtf8("actionB_add_line"))
        self.actionB_delete_line = QtGui.QAction(Parameter_water_q)
        self.actionB_delete_line.setObjectName(_fromUtf8("actionB_delete_line"))
        self.actionB_delete_lineTabTracer = QtGui.QAction(Parameter_water_q)
        self.actionB_delete_lineTabTracer.setObjectName(_fromUtf8("actionB_delete_lineTabTracer"))
        self.actionB_add_lineTabTracer = QtGui.QAction(Parameter_water_q)
        self.actionB_add_lineTabTracer.setObjectName(_fromUtf8("actionB_add_lineTabTracer"))
        self.actionB_phy_param = QtGui.QAction(Parameter_water_q)
        self.actionB_phy_param.setObjectName(_fromUtf8("actionB_phy_param"))
        self.actionB_meteo_param = QtGui.QAction(Parameter_water_q)
        self.actionB_meteo_param.setObjectName(_fromUtf8("actionB_meteo_param"))

        self.retranslateUi(Parameter_water_q)
        self.WaterQ.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Parameter_water_q)

    def retranslateUi(self, Parameter_water_q):
        Parameter_water_q.setWindowTitle(_translate("Parameter_water_q", "Parameters Water Quality", None))
        self.modeleQualiteEau.setItemText(0, _translate("Parameter_water_q", "TRANSPORT_PUR", None))
        self.modeleQualiteEau.setItemText(1, _translate("Parameter_water_q", "O2", None))
        self.modeleQualiteEau.setItemText(2, _translate("Parameter_water_q", "BIOMASS", None))
        self.modeleQualiteEau.setItemText(3, _translate("Parameter_water_q", "EUTRO", None))
        self.modeleQualiteEau.setItemText(4, _translate("Parameter_water_q", "MICROPOLE", None))
        self.modeleQualiteEau.setItemText(5, _translate("Parameter_water_q", "THERMIC", None))
        self.label_modeleQualiteEau.setText(_translate("Parameter_water_q", "Water quality module : ", None))
        self.presenceTraceurs.setText(_translate("Parameter_water_q", "Activation of the water quality module", None))
        self.label_nbTraceur.setText(_translate("Parameter_water_q", "Number of constituents : ", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Parameter_water_q", "Names of constituents", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Parameter_water_q", "Properties", None))
        self.b_add_lineTabTracer.setText(_translate("Parameter_water_q", "Add Line", None))
        self.b_delete_lineTabTracer.setText(_translate("Parameter_water_q", "Delete Line", None))
        self.WaterQ.setTabText(self.WaterQ.indexOf(self.tab), _translate("Parameter_water_q", "Choice of the water quality module", None))
        item = self.table_InitC.horizontalHeaderItem(0)
        item.setText(_translate("Parameter_water_q", "N° Bief", None))
        item = self.table_InitC.horizontalHeaderItem(1)
        item.setText(_translate("Parameter_water_q", "Abscisca", None))
        item = self.table_InitC.horizontalHeaderItem(2)
        item.setText(_translate("Parameter_water_q", "C°TRA1", None))
        self.b_add_line.setText(_translate("Parameter_water_q", "Add Line", None))
        self.b_delete_line.setText(_translate("Parameter_water_q", "Delete Line", None))
        self.WaterQ.setTabText(self.WaterQ.indexOf(self.tab_2), _translate("Parameter_water_q", "Initial Concentrations", None))
        self.optionCalculDiffusion_seo.setText(_translate("Parameter_water_q", "Seo & Cheong (1998)", None))
        self.optionCalculDiffusion_Fisher.setText(_translate("Parameter_water_q", "Fisher (1975)", None))
        self.LimitPente.setItemText(0, _translate("Parameter_water_q", "Yes", None))
        self.LimitPente.setItemText(1, _translate("Parameter_water_q", "No", None))
        self.optionCalculDiffusion_isawa.setText(_translate("Parameter_water_q", "Isawa & Aga (1991)", None))
        self.label_frequenceCouplHydroTracer.setText(_translate("Parameter_water_q", "Frequency for coupling :", None))
        self.label_ordreSchemaConvec.setText(_translate("Parameter_water_q", "Scheme order :", None))
        self.ordreSchemaConvec.setItemText(0, _translate("Parameter_water_q", "1", None))
        self.ordreSchemaConvec.setItemText(1, _translate("Parameter_water_q", "2", None))
        self.label_optionCalculDiffusion.setText(_translate("Parameter_water_q", "Diffusion method :", None))
        self.label_optionConvection.setText(_translate("Parameter_water_q", "Convection method :", None))
        self.optionConvection.setItemText(0, _translate("Parameter_water_q", "HYP1FA fnc", None))
        self.optionConvection.setItemText(1, _translate("Parameter_water_q", "HYP1FA fc", None))
        self.optionConvection.setItemText(2, _translate("Parameter_water_q", "FV", None))
        self.optionCalculDiffusion_default.setText(_translate("Parameter_water_q", "Constant diffussion coef. :", None))
        self.optionCalculDiffusion_liu.setText(_translate("Parameter_water_q", "Liu (1977)", None))
        self.optionCalculDiffusion_deng.setText(_translate("Parameter_water_q", "Deng & al. (2001)", None))
        self.optionCalculDiffusion_keefer.setText(_translate("Parameter_water_q", "McQuivey & Keefer", None))
        self.label_LimitPente.setText(_translate("Parameter_water_q", "Slope limiter", None))
        self.optionCalculDiffusion_Mirasol.setText(_translate("Parameter_water_q", "Koussis & Rodriguez-Mirasol (1998)", None))
        self.optionCalculDiffusion_elder.setText(_translate("Parameter_water_q", "Elder (1959)", None))
        self.optionCalculDiffusion_magazine.setText(_translate("Parameter_water_q", "Magazine & al. (1988)", None))
        self.label_paramW.setText(_translate("Parameter_water_q", "Parameter W", None))
        self.optionCalculDiffusion_falconer.setText(_translate("Parameter_water_q", "Kashefipur & Falconer (2002)", None))
        item = self.table_conv_diff.horizontalHeaderItem(0)
        item.setText(_translate("Parameter_water_q", "Tracer name", None))
        item = self.table_conv_diff.horizontalHeaderItem(1)
        item.setText(_translate("Parameter_water_q", "Diffusion", None))
        item = self.table_conv_diff.horizontalHeaderItem(2)
        item.setText(_translate("Parameter_water_q", "Convection", None))
        self.b_phy_param.setText(_translate("Parameter_water_q", "Physical parameters", None))
        self.b_meteo_param.setText(_translate("Parameter_water_q", "Meteo parameters", None))
        self.WaterQ.setTabText(self.WaterQ.indexOf(self.tab_3), _translate("Parameter_water_q", "General Parameters", None))
        self.concentInit.setText(_translate("Parameter_water_q", "Initial Concentration", None))
        self.loiTracer.setText(_translate("Parameter_water_q", "Tracer law used", None))
        self.concentrations.setText(_translate("Parameter_water_q", "Concentrations", None))
        self.bilanTracer.setText(_translate("Parameter_water_q", "Constituants balance", None))
        self.WaterQ.setTabText(self.WaterQ.indexOf(self.tab_5), _translate("Parameter_water_q", "Results", None))
        self.actionB_add_line.setText(_translate("Parameter_water_q", "b_add_line", None))
        self.actionB_delete_line.setText(_translate("Parameter_water_q", "b_delete_line", None))
        self.actionB_delete_lineTabTracer.setText(_translate("Parameter_water_q", "b_delete_lineTabTracer", None))
        self.actionB_add_lineTabTracer.setText(_translate("Parameter_water_q", "b_add_lineTabTracer", None))
        self.actionB_phy_param.setText(_translate("Parameter_water_q", "b_phy_param", None))
        self.actionB_meteo_param.setText(_translate("Parameter_water_q", "b_meteo_param", None))

