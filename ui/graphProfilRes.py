# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphProfilRes.ui'
#
# Created: Thu Dec 21 18:11:34 2017
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

class Ui_ProfilGraphRes(object):
    def setupUi(self, ProfilGraphRes):
        ProfilGraphRes.setObjectName(_fromUtf8("ProfilGraphRes"))
        ProfilGraphRes.resize(814, 700)
        self.gridLayout = QtGui.QGridLayout(ProfilGraphRes)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bt_reculTot = QtGui.QPushButton(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_reculTot.sizePolicy().hasHeightForWidth())
        self.bt_reculTot.setSizePolicy(sizePolicy)
        self.bt_reculTot.setDefault(False)
        self.bt_reculTot.setObjectName(_fromUtf8("bt_reculTot"))
        self.horizontalLayout_2.addWidget(self.bt_reculTot)
        self.bt_recul = QtGui.QPushButton(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_recul.sizePolicy().hasHeightForWidth())
        self.bt_recul.setSizePolicy(sizePolicy)
        self.bt_recul.setObjectName(_fromUtf8("bt_recul"))
        self.horizontalLayout_2.addWidget(self.bt_recul)
        self.bt_av = QtGui.QPushButton(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_av.sizePolicy().hasHeightForWidth())
        self.bt_av.setSizePolicy(sizePolicy)
        self.bt_av.setObjectName(_fromUtf8("bt_av"))
        self.horizontalLayout_2.addWidget(self.bt_av)
        self.bt_avTot = QtGui.QPushButton(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_avTot.sizePolicy().hasHeightForWidth())
        self.bt_avTot.setSizePolicy(sizePolicy)
        self.bt_avTot.setObjectName(_fromUtf8("bt_avTot"))
        self.horizontalLayout_2.addWidget(self.bt_avTot)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ProfilGraphRes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_Title = QtGui.QLabel(ProfilGraphRes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName(_fromUtf8("label_Title"))
        self.horizontalLayout.addWidget(self.label_Title)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comboBox_State = QtGui.QComboBox(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_State.sizePolicy().hasHeightForWidth())
        self.comboBox_State.setSizePolicy(sizePolicy)
        self.comboBox_State.setObjectName(_fromUtf8("comboBox_State"))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_State)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.comboBox_Scenar = QtGui.QComboBox(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Scenar.sizePolicy().hasHeightForWidth())
        self.comboBox_Scenar.setSizePolicy(sizePolicy)
        self.comboBox_Scenar.setObjectName(_fromUtf8("comboBox_Scenar"))
        self.comboBox_Scenar.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_Scenar)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.comboBox_Time = QtGui.QComboBox(ProfilGraphRes)
        self.comboBox_Time.setObjectName(_fromUtf8("comboBox_Time"))
        self.horizontalLayout_5.addWidget(self.comboBox_Time)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.widget_figure = QtGui.QWidget(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_figure.sizePolicy().hasHeightForWidth())
        self.widget_figure.setSizePolicy(sizePolicy)
        self.widget_figure.setObjectName(_fromUtf8("widget_figure"))
        self.verticalLayout.addWidget(self.widget_figure)
        self.widget_toolsbar = QtGui.QWidget(ProfilGraphRes)
        self.widget_toolsbar.setObjectName(_fromUtf8("widget_toolsbar"))
        self.verticalLayout.addWidget(self.widget_toolsbar)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(ProfilGraphRes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_hmax = QtGui.QLabel(ProfilGraphRes)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_hmax.setFont(font)
        self.label_hmax.setObjectName(_fromUtf8("label_hmax"))
        self.horizontalLayout_3.addWidget(self.label_hmax)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableWidget_RES = QtGui.QTableWidget(ProfilGraphRes)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_RES.sizePolicy().hasHeightForWidth())
        self.tableWidget_RES.setSizePolicy(sizePolicy)
        self.tableWidget_RES.setObjectName(_fromUtf8("tableWidget_RES"))
        self.tableWidget_RES.setColumnCount(2)
        self.tableWidget_RES.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_RES.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_RES.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget_RES)
        self.bt_exportCSV = QtGui.QPushButton(ProfilGraphRes)
        self.bt_exportCSV.setObjectName(_fromUtf8("bt_exportCSV"))
        self.verticalLayout_2.addWidget(self.bt_exportCSV)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.actionBt_reculTot = QtGui.QAction(ProfilGraphRes)
        self.actionBt_reculTot.setObjectName(_fromUtf8("actionBt_reculTot"))
        self.actionBt_recul = QtGui.QAction(ProfilGraphRes)
        self.actionBt_recul.setObjectName(_fromUtf8("actionBt_recul"))
        self.actionBt_av = QtGui.QAction(ProfilGraphRes)
        self.actionBt_av.setObjectName(_fromUtf8("actionBt_av"))
        self.actionBt_avTot = QtGui.QAction(ProfilGraphRes)
        self.actionBt_avTot.setObjectName(_fromUtf8("actionBt_avTot"))
        self.actionBt_exportCSV = QtGui.QAction(ProfilGraphRes)
        self.actionBt_exportCSV.setObjectName(_fromUtf8("actionBt_exportCSV"))
        self.actionComboBox_State = QtGui.QAction(ProfilGraphRes)
        self.actionComboBox_State.setObjectName(_fromUtf8("actionComboBox_State"))
        self.actionComboBox_Scenar = QtGui.QAction(ProfilGraphRes)
        self.actionComboBox_Scenar.setObjectName(_fromUtf8("actionComboBox_Scenar"))
        self.actionTableWidget_RES = QtGui.QAction(ProfilGraphRes)
        self.actionTableWidget_RES.setObjectName(_fromUtf8("actionTableWidget_RES"))
        self.actionComboBox_Time = QtGui.QAction(ProfilGraphRes)
        self.actionComboBox_Time.setObjectName(_fromUtf8("actionComboBox_Time"))

        self.retranslateUi(ProfilGraphRes)
        QtCore.QObject.connect(self.bt_recul, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_recul.trigger)
        QtCore.QObject.connect(self.bt_reculTot, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_reculTot.trigger)
        QtCore.QObject.connect(self.bt_av, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_av.trigger)
        QtCore.QObject.connect(self.bt_avTot, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_avTot.trigger)
        QtCore.QObject.connect(self.bt_exportCSV, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionBt_exportCSV.trigger)
        QtCore.QObject.connect(self.comboBox_State, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_State.trigger)
        QtCore.QObject.connect(self.comboBox_Scenar, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_Scenar.trigger)
        QtCore.QObject.connect(self.comboBox_Time, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.actionComboBox_Time.trigger)
        QtCore.QMetaObject.connectSlotsByName(ProfilGraphRes)

    def retranslateUi(self, ProfilGraphRes):
        ProfilGraphRes.setWindowTitle(_translate("ProfilGraphRes", "Profile Results", None))
        self.bt_reculTot.setText(_translate("ProfilGraphRes", "<<", None))
        self.bt_recul.setText(_translate("ProfilGraphRes", "<", None))
        self.bt_av.setText(_translate("ProfilGraphRes", ">", None))
        self.bt_avTot.setText(_translate("ProfilGraphRes", ">>", None))
        self.label.setText(_translate("ProfilGraphRes", "Title :", None))
        self.label_Title.setText(_translate("ProfilGraphRes", "Toto", None))
        self.comboBox_State.setItemText(0, _translate("ProfilGraphRes", "Transcritical unsteady", None))
        self.comboBox_State.setItemText(1, _translate("ProfilGraphRes", "Steady", None))
        self.comboBox_State.setItemText(2, _translate("ProfilGraphRes", "Unsteady", None))
        self.comboBox_Scenar.setItemText(0, _translate("ProfilGraphRes", "Scenar", None))
        self.label_2.setText(_translate("ProfilGraphRes", "Hmax :", None))
        self.label_hmax.setText(_translate("ProfilGraphRes", "Hmax", None))
        item = self.tableWidget_RES.horizontalHeaderItem(0)
        item.setText(_translate("ProfilGraphRes", "X", None))
        item = self.tableWidget_RES.horizontalHeaderItem(1)
        item.setText(_translate("ProfilGraphRes", "Z", None))
        self.bt_exportCSV.setText(_translate("ProfilGraphRes", "Profil export CSV", None))
        self.actionBt_reculTot.setText(_translate("ProfilGraphRes", "bt_reculTot", None))
        self.actionBt_recul.setText(_translate("ProfilGraphRes", "bt_recul", None))
        self.actionBt_av.setText(_translate("ProfilGraphRes", "bt_av", None))
        self.actionBt_avTot.setText(_translate("ProfilGraphRes", "bt_avTot", None))
        self.actionBt_exportCSV.setText(_translate("ProfilGraphRes", "bt_exportCSV", None))
        self.actionComboBox_State.setText(_translate("ProfilGraphRes", "comboBox_State", None))
        self.actionComboBox_Scenar.setText(_translate("ProfilGraphRes", "comboBox_Scenar", None))
        self.actionTableWidget_RES.setText(_translate("ProfilGraphRes", "tableWidget_RES", None))
        self.actionComboBox_Time.setText(_translate("ProfilGraphRes", "comboBox_Time", None))

