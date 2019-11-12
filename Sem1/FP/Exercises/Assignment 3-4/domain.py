from validations import *

def get_real_part(number):
    return number["real"]
def get_imaginary_part(number):
    return number["imaginary"]

def set_real_part(number,value):
    number["real"] = value
def set_imaginary_part(number,value):
    number["imaginary"] = value

def create_complex_number(a,b):
    if not is_integer(a) or not is_integer(b):
        raise ValueError("Invalid data")
    return {"real":a,"imaginary":b}

def init_list():
    complexList = []
    complexList.append(create_complex_number(1,-1))
    complexList.append(create_complex_number(-2,-1))
    complexList.append(create_complex_number(0,1))
    complexList.append(create_complex_number(1,-0))
    complexList.append(create_complex_number(1,2))
    complexList.append(create_complex_number(-9,-3))
    complexList.append(create_complex_number(4,-5))
    complexList.append(create_complex_number(-1,-1))
    complexList.append(create_complex_number(2,3))
    complexList.append(create_complex_number(-2,-1))
    complexList.append(create_complex_number(6,-0))
    return complexList

def to_str(number):
    if get_imaginary_part(number) >= 0:
        return str(get_real_part(number)) + "+" + str(get_imaginary_part(number)) + "i"
    else:
        return str(get_real_part(number)) + str(get_imaginary_part(number)) + "i"
