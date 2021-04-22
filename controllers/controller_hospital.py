from model import hospital

hospital = hospital.Hospital("")


def create_hospital(name):
    hospital.hospital_name = name


def append_doctor(doctor_to_be_added):
    hospital.add_doctor(doctor_to_be_added)


def get_doctor_by_name(doctor_to_find):
    for doctor in hospital.doctors:
        if doctor.doctor_name == doctor_to_find:
            return doctor


def get_doctor_by_dni(dni_to_find):
    for doctor in hospital.doctors:
        if doctor.doctor_dni == dni_to_find:
            return doctor
