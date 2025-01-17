# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(1064, 931)
        SettingsWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 6, 1, 1)
        self.drp_device = QtWidgets.QComboBox(self.centralwidget)
        self.drp_device.setObjectName("drp_device")
        self.gridLayout.addWidget(self.drp_device, 1, 7, 1, 1)
        self.drp_sim = QtWidgets.QComboBox(self.centralwidget)
        self.drp_sim.setEditable(False)
        self.drp_sim.setObjectName("drp_sim")
        self.drp_sim.addItem("")
        self.drp_sim.addItem("")
        self.drp_sim.addItem("")
        self.gridLayout.addWidget(self.drp_sim, 1, 0, 1, 1)
        self.pb_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pb_clear.setObjectName("pb_clear")
        self.gridLayout.addWidget(self.pb_clear, 1, 3, 1, 1)
        self.drp_models = QtWidgets.QComboBox(self.centralwidget)
        self.drp_models.setEditable(False)
        self.drp_models.setObjectName("drp_models")
        self.drp_models.addItem("")
        self.drp_models.setItemText(0, "")
        self.gridLayout.addWidget(self.drp_models, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.drp_class = QtWidgets.QComboBox(self.centralwidget)
        self.drp_class.setObjectName("drp_class")
        self.drp_class.addItem("")
        self.drp_class.setItemText(0, "")
        self.drp_class.addItem("")
        self.drp_class.addItem("")
        self.drp_class.addItem("")
        self.drp_class.addItem("")
        self.drp_class.addItem("")
        self.drp_class.addItem("")
        self.gridLayout.addWidget(self.drp_class, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        self.l_mode = QtWidgets.QLabel(self.centralwidget)
        self.l_mode.setMaximumSize(QtCore.QSize(150, 16777215))
        self.l_mode.setObjectName("l_mode")
        self.gridLayout.addWidget(self.l_mode, 0, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.b_createusermodel = QtWidgets.QPushButton(self.centralwidget)
        self.b_createusermodel.setObjectName("b_createusermodel")
        self.gridLayout.addWidget(self.b_createusermodel, 1, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_widget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy)
        self.table_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table_widget.setWordWrap(False)
        self.table_widget.setCornerButtonEnabled(False)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(5)
        self.table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        self.table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.table_widget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.table_widget)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_manual = QtWidgets.QLabel(self.centralwidget)
        self.l_manual.setTextFormat(QtCore.Qt.RichText)
        self.l_manual.setAlignment(QtCore.Qt.AlignCenter)
        self.l_manual.setOpenExternalLinks(True)
        self.l_manual.setObjectName("l_manual")
        self.gridLayout_2.addWidget(self.l_manual, 1, 5, 1, 1)
        self.b_deleteModel = QtWidgets.QPushButton(self.centralwidget)
        self.b_deleteModel.setEnabled(False)
        self.b_deleteModel.setObjectName("b_deleteModel")
        self.gridLayout_2.addWidget(self.b_deleteModel, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.cb_show_inherited = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_show_inherited.setChecked(True)
        self.cb_show_inherited.setObjectName("cb_show_inherited")
        self.gridLayout_2.addWidget(self.cb_show_inherited, 0, 0, 1, 1)
        self.l_currentmodel = QtWidgets.QLabel(self.centralwidget)
        self.l_currentmodel.setObjectName("l_currentmodel")
        self.gridLayout_2.addWidget(self.l_currentmodel, 1, 3, 1, 1)
        self.b_revert = QtWidgets.QPushButton(self.centralwidget)
        self.b_revert.setObjectName("b_revert")
        self.gridLayout_2.addWidget(self.b_revert, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.l_displayname = QtWidgets.QLabel(self.centralwidget)
        self.l_displayname.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_displayname.setFont(font)
        self.l_displayname.setAlignment(QtCore.Qt.AlignCenter)
        self.l_displayname.setObjectName("l_displayname")
        self.verticalLayout.addWidget(self.l_displayname)
        self.l_name = QtWidgets.QLabel(self.centralwidget)
        self.l_name.setEnabled(False)
        self.l_name.setAlignment(QtCore.Qt.AlignCenter)
        self.l_name.setObjectName("l_name")
        self.verticalLayout.addWidget(self.l_name)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.t_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_info.sizePolicy().hasHeightForWidth())
        self.t_info.setSizePolicy(sizePolicy)
        self.t_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.t_info.setWordWrap(True)
        self.t_info.setObjectName("t_info")
        self.verticalLayout.addWidget(self.t_info)
        self.cb_enable = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_enable.setObjectName("cb_enable")
        self.verticalLayout.addWidget(self.cb_enable)
        self.l_value = QtWidgets.QLabel(self.centralwidget)
        self.l_value.setObjectName("l_value")
        self.verticalLayout.addWidget(self.l_value)
        self.tb_value = QtWidgets.QLineEdit(self.centralwidget)
        self.tb_value.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.tb_value.setObjectName("tb_value")
        self.verticalLayout.addWidget(self.tb_value)
        self.slider_float = QtWidgets.QSlider(self.centralwidget)
        self.slider_float.setMaximumSize(QtCore.QSize(200, 16777215))
        self.slider_float.setOrientation(QtCore.Qt.Horizontal)
        self.slider_float.setObjectName("slider_float")
        self.verticalLayout.addWidget(self.slider_float)
        self.l_sliderfactor = QtWidgets.QLabel(self.centralwidget)
        self.l_sliderfactor.setEnabled(True)
        self.l_sliderfactor.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.l_sliderfactor.setFont(font)
        self.l_sliderfactor.setStyleSheet("color: #ff0000;")
        self.l_sliderfactor.setWordWrap(True)
        self.l_sliderfactor.setObjectName("l_sliderfactor")
        self.verticalLayout.addWidget(self.l_sliderfactor)
        self.b_browse = QtWidgets.QPushButton(self.centralwidget)
        self.b_browse.setObjectName("b_browse")
        self.verticalLayout.addWidget(self.b_browse)
        self.b_gainoverrides = QtWidgets.QPushButton(self.centralwidget)
        self.b_gainoverrides.setObjectName("b_gainoverrides")
        self.verticalLayout.addWidget(self.b_gainoverrides)
        self.b_usb_button = QtWidgets.QPushButton(self.centralwidget)
        self.b_usb_button.setObjectName("b_usb_button")
        self.verticalLayout.addWidget(self.b_usb_button)
        self.drp_valuebox = QtWidgets.QComboBox(self.centralwidget)
        self.drp_valuebox.setObjectName("drp_valuebox")
        self.verticalLayout.addWidget(self.drp_valuebox)
        self.b_update = QtWidgets.QPushButton(self.centralwidget)
        self.b_update.setMaximumSize(QtCore.QSize(200, 16777215))
        self.b_update.setObjectName("b_update")
        self.verticalLayout.addWidget(self.b_update)
        spacerItem2 = QtWidgets.QSpacerItem(150, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.b_getcurrentmodel = QtWidgets.QPushButton(self.centralwidget)
        self.b_getcurrentmodel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.b_getcurrentmodel.setObjectName("b_getcurrentmodel")
        self.verticalLayout.addWidget(self.b_getcurrentmodel)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "TelemFFB Settings Manager"))
        self.label_2.setText(_translate("SettingsWindow", "Device Scope:"))
        self.drp_sim.setItemText(0, _translate("SettingsWindow", "DCS"))
        self.drp_sim.setItemText(1, _translate("SettingsWindow", "IL2"))
        self.drp_sim.setItemText(2, _translate("SettingsWindow", "MSFS"))
        self.pb_clear.setText(_translate("SettingsWindow", "Clear Selection"))
        self.label_5.setText(_translate("SettingsWindow", "Class"))
        self.drp_class.setItemText(1, _translate("SettingsWindow", "PropellerAircraft"))
        self.drp_class.setItemText(2, _translate("SettingsWindow", "TurbopropAircraft"))
        self.drp_class.setItemText(3, _translate("SettingsWindow", "JetAircraft"))
        self.drp_class.setItemText(4, _translate("SettingsWindow", "GliderAircraft"))
        self.drp_class.setItemText(5, _translate("SettingsWindow", "Helicopter"))
        self.drp_class.setItemText(6, _translate("SettingsWindow", "HPGHelicopter"))
        self.l_mode.setText(_translate("SettingsWindow", "Model"))
        self.label_6.setText(_translate("SettingsWindow", "Model"))
        self.label_3.setText(_translate("SettingsWindow", "Edit Mode:"))
        self.label_4.setText(_translate("SettingsWindow", "Simulator"))
        self.b_createusermodel.setToolTip(_translate("SettingsWindow", "<html><head/><body><p>Select the <span style=\" font-weight:600;\">Simulator</span> and, optionally, the <span style=\" font-weight:600;\">Class</span> for the new aircraft you want to add.</p><p><br/></p><p>Then press this button and then fill out the resulting form.</p></body></html>"))
        self.b_createusermodel.setText(_translate("SettingsWindow", "Create New Model"))
        self.table_widget.setSortingEnabled(False)
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("SettingsWindow", "New Column"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("SettingsWindow", "New Column"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("SettingsWindow", "New Column"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate("SettingsWindow", "New Column"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate("SettingsWindow", "New Column"))
        self.l_manual.setText(_translate("SettingsWindow", "<a href=\"https://docs.google.com/document/d/1YL5DLkiTxlaNx_zKHEYSs25PjmGtQ6_WZDk58_SGt8Y\">Read manual for details</a>"))
        self.b_deleteModel.setText(_translate("SettingsWindow", "Delete User Model"))
        self.label_9.setText(_translate("SettingsWindow", "Currently Editing:"))
        self.cb_show_inherited.setText(_translate("SettingsWindow", "Show Defaults"))
        self.l_currentmodel.setText(_translate("SettingsWindow", "TextLabel"))
        self.b_revert.setText(_translate("SettingsWindow", "Revert Changes"))
        self.l_displayname.setText(_translate("SettingsWindow", "Select a Row to Edit"))
        self.l_name.setText(_translate("SettingsWindow", "TextLabel"))
        self.t_info.setText(_translate("SettingsWindow", "Desc"))
        self.cb_enable.setText(_translate("SettingsWindow", "Enable"))
        self.l_value.setText(_translate("SettingsWindow", "Value:"))
        self.l_sliderfactor.setText(_translate("SettingsWindow", "Raw value shown above.  Slider ranges in the main window are multiplied by the factor value for more usable settings ranges"))
        self.b_browse.setText(_translate("SettingsWindow", "Browse..."))
        self.b_gainoverrides.setText(_translate("SettingsWindow", "Configure Gain Overrides"))
        self.b_usb_button.setText(_translate("SettingsWindow", "PushButton"))
        self.b_update.setText(_translate("SettingsWindow", "Update Value"))
        self.label_7.setText(_translate("SettingsWindow", "Source checkbox must be checked"))
        self.label_8.setText(_translate("SettingsWindow", "to allow selection and editing"))
        self.b_getcurrentmodel.setToolTip(_translate("SettingsWindow", "<html><head/><body><p>Select this button while a sim is running to recall the currently loaded aircraft.</p><p><br/></p><p>With no sim running, this button has no effect.</p></body></html>"))
        self.b_getcurrentmodel.setText(_translate("SettingsWindow", "Get Current Model"))
