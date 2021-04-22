from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QAction
from GUI import doctor_form, hospital_form, search_doctor_dni, search_doctor_name
import sys


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1089, 829)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.welcome_sign = QtWidgets.QLabel(self.centralwidget)
        self.welcome_sign.setGeometry(QtCore.QRect(0, 40, 1071, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.welcome_sign.setFont(font)
        self.welcome_sign.setObjectName("welcome_sign")

        self.doctors_image = QtWidgets.QLabel(self.centralwidget)
        self.doctors_image.setGeometry(QtCore.QRect(190, 100, 721, 491))
        self.doctors_image.setText("")
        self.doctors_image.setPixmap(QtGui.QPixmap("../SIH SYSTEM UI FILES/doctores.jpg"))
        self.doctors_image.setScaledContents(True)
        self.doctors_image.setObjectName("doctors_image")

        self.instructions_sih = QtWidgets.QLabel(self.centralwidget)
        self.instructions_sih.setGeometry(QtCore.QRect(0, 630, 1071, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.instructions_sih.setFont(font)
        self.instructions_sih.setObjectName("instructions_sih")

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 21))
        self.menubar.setObjectName("menubar")

        self.menuHospital = QtWidgets.QMenu(self.menubar)
        self.menuHospital.setObjectName("menuHospital")

        self.menu_doctor = QtWidgets.QMenu(self.menubar)
        self.menu_doctor.setObjectName("menu_doctor")

        self.menu_search_doctor = QtWidgets.QMenu(self.menu_doctor)
        self.menu_search_doctor.setObjectName("menu_search_doctor")

        main_window.setMenuBar(self.menubar)
        self.action_add_hospital = QtWidgets.QAction(main_window)
        self.action_add_hospital.setObjectName("action_add_hospital")

        self.actionBuscar_hospital = QtWidgets.QAction(main_window)
        self.actionBuscar_hospital.setObjectName("actionBuscar_hospital")

        self.action_add_doctor = QtWidgets.QAction(main_window)
        self.action_add_doctor.setObjectName("action_add_doctor")

        self.actionPor_dni = QtWidgets.QAction(main_window)
        self.actionPor_dni.setObjectName("actionPor_dni")

        self.action_search_by_dni = QtWidgets.QAction(main_window)
        self.action_search_by_dni.setObjectName("action_search_by_dni")

        self.action_search_by_full_name = QtWidgets.QAction(main_window)
        self.action_search_by_full_name.setObjectName("action_search_by_full_name")

        self.menuHospital.addAction(self.action_add_hospital)
        self.menuHospital.triggered.connect(self.show_add_hospital_form)

        self.menu_search_doctor.addAction(self.action_search_by_dni)
        self.menu_search_doctor.addAction(self.action_search_by_full_name)
        self.action_search_by_dni.triggered.connect(self.show_doctor_search_dni_form)
        self.action_search_by_full_name.triggered.connect(self.show_doctor_search_fullname_form)

        self.menu_doctor.addAction(self.action_add_doctor)
        self.menu_doctor.addAction(self.menu_search_doctor.menuAction())
        self.action_add_doctor.triggered.connect(self.show_add_doctor_form)

        self.menubar.addAction(self.menuHospital.menuAction())
        self.menubar.addAction(self.menu_doctor.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Sistema de información hospitalaria SIH"))
        self.welcome_sign.setText(_translate("main_window",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Bienvenido a la interfaz del sistema de información hospitalaria SIH </span></p></body></html>"))
        self.instructions_sih.setText(_translate("main_window",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Por favor seleccione una de las opciones de la esquina superior izquierda</span></p></body></html>"))
        self.menuHospital.setTitle(_translate("main_window", "Hospital"))
        self.menu_doctor.setTitle(_translate("main_window", "Doctor"))
        self.menu_search_doctor.setTitle(_translate("main_window", "Buscar doctor"))
        self.action_add_hospital.setText(_translate("main_window", "Agregar hospital"))
        self.actionBuscar_hospital.setText(_translate("main_window", "Buscar hospital"))
        self.action_add_doctor.setText(_translate("main_window", "Añadir doctor"))
        self.actionPor_dni.setText(_translate("main_window", "Por dni"))
        self.action_search_by_dni.setText(_translate("main_window", "Por DNI"))
        self.action_search_by_full_name.setText(_translate("main_window", "Por nombre completo"))

    def show_add_hospital_form(self):
        self.add_hospital_window = QtWidgets.QMainWindow()
        self.ui_hospital = hospital_form.Ui_add_hospital_form()
        self.ui_hospital.setupUi(self.add_hospital_window)
        self.add_hospital_window.show()

    def show_add_doctor_form(self):
        self.add_doctor_window = QtWidgets.QMainWindow()
        self.ui_doctor = doctor_form.Ui_add_doctor_form()
        self.ui_doctor.setupUi(self.add_doctor_window)
        self.add_doctor_window.show()

    def show_doctor_search_dni_form(self):
        self.search_doctor_dni_window = QtWidgets.QMainWindow()
        self.ui_search_doctor_dni = search_doctor_dni.Ui_doctor_search_form()
        self.ui_search_doctor_dni.setupUi(self.search_doctor_dni_window)
        self.search_doctor_dni_window.show()

    def show_doctor_search_fullname_form(self):
        self.search_doctor_fullname_window = QtWidgets.QMainWindow()
        self.ui_search_doctor_name = search_doctor_name.Ui_doctor_search_form()
        self.ui_search_doctor_name.setupUi(self.search_doctor_fullname_window)
        self.search_doctor_fullname_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
