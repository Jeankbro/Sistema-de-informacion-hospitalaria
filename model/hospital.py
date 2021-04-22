class Hospital():
    def __init__(self, hospital_name):
        self.__hospital_name = hospital_name
        self.__doctors = []

    @property
    def hospital_name(self):
        return self.__hospital_name

    @hospital_name.setter
    def hospital_name(self, hospital_name):
        self.__hospital_name = hospital_name

    @property
    def doctors(self):
        return self.__doctors

    @doctors.setter
    def doctors(self, doctor):
        self.doctors.append(doctor)

    def add_doctor(self, doctor):
        self.doctors = doctor





