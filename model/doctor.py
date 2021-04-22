class Doctor():
    def __init__(self, doctor_name, doctor_dni, doctor_specialty):
        self.__doctor_name = doctor_name
        self.__doctor_dni = doctor_dni
        self.__doctor_specialty = doctor_specialty

    @property
    def doctor_name(self):
        return self.__doctor_name

    @doctor_name.setter
    def doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    @property
    def doctor_dni(self):
        return self.__doctor_dni

    @doctor_dni.setter
    def doctor_dni(self, doctor_dni):
        self.__doctor_dni = doctor_dni

    @property
    def doctor_specialty(self):
        return self.__doctor_specialty

    @doctor_specialty.setter
    def doctor_specialty(self, doctor_specialty):
        self.__doctor_specialty = doctor_specialty

    #Método de prueba
    def show_doctor_info(self):
        return self.__doctor_name, self.__doctor_dni, self.__doctor_specialty
