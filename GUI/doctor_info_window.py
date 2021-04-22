# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctor_info_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from controllers import controller_hospital
from PyQt5.QtWidgets import QMessageBox


class Ui_doctor_info_window(object):
    def setupUi(self, doctor_info_window):
        doctor_info_window.setObjectName("doctor_info_window")
        doctor_info_window.resize(772, 286)
        self.doctor_info_section = QtWidgets.QGroupBox(doctor_info_window)
        self.doctor_info_section.setGeometry(QtCore.QRect(10, 20, 741, 241))
        self.doctor_info_section.setObjectName("doctor_info_section")
        self.doctor_info_table = QtWidgets.QTableWidget(self.doctor_info_section)
        self.doctor_info_table.setGeometry(QtCore.QRect(20, 30, 701, 191))
        self.doctor_info_table.setObjectName("doctor_info_table")
        self.doctor_info_table.setColumnCount(4)
        self.doctor_info_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_info_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_info_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_info_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.doctor_info_table.setHorizontalHeaderItem(3, item)

        self.retranslateUi(doctor_info_window)
        QtCore.QMetaObject.connectSlotsByName(doctor_info_window)

    def retranslateUi(self, doctor_info_window):
        _translate = QtCore.QCoreApplication.translate
        doctor_info_window.setWindowTitle(_translate("doctor_info_window", "Información del doctor(a)"))
        self.doctor_info_section.setTitle(_translate("doctor_info_window", "Información del doctor(a)"))
        item = self.doctor_info_table.horizontalHeaderItem(0)
        item.setText(_translate("doctor_info_window", "Nombre completo"))
        item = self.doctor_info_table.horizontalHeaderItem(1)
        item.setText(_translate("doctor_info_window", "Especialización"))
        item = self.doctor_info_table.horizontalHeaderItem(2)
        item.setText(_translate("doctor_info_window", "DNI"))
        item = self.doctor_info_table.horizontalHeaderItem(3)
        item.setText(_translate("doctor_info_window", "Hospital"))

    def show_message(self, message, type_message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setIcon(type_message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def load_data(self, doctor):
        if doctor is None:
            self.show_message("El doctor(a) no pudo ser encontrado(a), intente de nuevo.", QMessageBox.Critical)
        else:
            self.doctor_info_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(doctor.doctor_name)))
            self.doctor_info_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(doctor.doctor_specialty)))
            self.doctor_info_table.setItem(0, 2, QtWidgets.QTableWidgetItem(str(doctor.doctor_dni)))
            self.doctor_info_table.setItem(0, 3, QtWidgets.QTableWidgetItem(str(controller_hospital.hospital.hospital_name)))

    def get_doctor_by_name(self, doctor):
        doctor_searched = controller_hospital.get_doctor_by_name(doctor)
        self.load_data(doctor_searched)

    def get_doctor_by_dni(self, dni):
        doctor_searched = controller_hospital.get_doctor_by_dni(dni)
        self.load_data(doctor_searched)




