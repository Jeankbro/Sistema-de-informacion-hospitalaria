from controllers import controller_hospital


def create_doctor(name, dni, specialty):
    from model import doctor
    doctor_name = name
    doctor_dni = dni
    doctor_specialty = specialty

    doctor = doctor.Doctor(doctor_name, doctor_dni, doctor_specialty)
    append_doctor(doctor)


def append_doctor(doctor):
    controller_hospital.append_doctor(doctor)



