from controllers import controller_hospital


def create_doctor(name, dni, specialty):
    from model import doctor
    doctor_name = name
    doctor_dni = dni
    doctor_specialty = specialty

    doctor = doctor.Doctor(doctor_name, doctor_dni, doctor_specialty)
    controller_hospital.append_doctor(doctor)

    return doctor


