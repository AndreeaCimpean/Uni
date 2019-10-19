import math

def get_real_part(z):
    return z['real']
def get_imaginary_part(z):
    return z['imaginary']
def set_real_part(z,a):
    z['real'] = a
def set_imaginary_part(z,b):
    z['imaginary'] = b

def print_menu():
    print(" ")
    print("1. Read numbers")
    print("2. Show all numbers")
    print("3. Sequences with some properties")
    print("4. Exit")

def create_number(a,b):
    '''
    Create a complex number
    params:
        a - the real part
        b - the imaginary part
    output
        the number as a dict
    '''
    return {"real":a,"imaginary":b} 

def init_list_of_numbers():
    '''
    Create an intial list of complex numbers
    no params
    outbut:
        a list of complex numbers
    '''
    lst = []
    lst.append(create_number(1,2))
    lst.append(create_number(3,-2))
    lst.append(create_number(-1,-2))
    lst.append(create_number(1,-2))
    lst.append(create_number(-1,2))
    lst.append(create_number(6,5))
    lst.append(create_number(-1,3))
    lst.append(create_number(3,4))
    lst.append(create_number(0,0))
    lst.append(create_number(-1,-4))
    lst.append(create_number(1,2))
    return lst

def show_all_numbers(numbers):
    for i in numbers:
        if get_imaginary_part(i) >= 0:
            print(str(get_real_part(i)) + '+' + str(get_imaginary_part(i)) + 'i')
        else:
            print(str(get_real_part(i)) + str(get_imaginary_part(i)) + 'i')

def read_a_number():
    a = int(input("real_part="))
    b = int(input("imaginary_part="))
    return create_number(a,b)


def read_a_list_of_numbers(numbers):
    while True:
        numbers.append(read_a_number())
        while True:
            print("Want to add another number? (Y/N)")
            choice = (input(">"))
            if choice == "N":
                return
            elif choice != "Y":
                print("Invalid command")
            else:
                break

def modulus(z):
    '''
    Get the modulus of a complex number
    params:
        z-the complex number
    output
        the modulus of z
    '''
    return math.sqrt(get_real_part(z)*get_real_part(z)+get_imaginary_part(z)*get_imaginary_part(z))

def isPrime(n):
    '''
    Check if a number is prime
    params:
        n - the number (!might be rational)
    output
        True - if the number is prime
        False - if the number is not prime
    '''
    if n != int(n):
        return False
    else:
        n = int(n)
    if n <= 1:
        return False
    else:
        for d in range(2,n//2+1):
            if int(n)%d == 0:
                return False
    return True

def get_longest_sequence_same_modulus(numbers):
    '''
    Get the longest sequence of numbers with the same modulus
    params:
        numbers-the list with all the numbers we have
    output
        None there isn't such a sequence
        the longerst sequence otherwise
    '''
    maxlength = -1
    start_position = 0
    p = 0
    length = 1
    m = modulus(numbers[0])
    for i in range(1,len(numbers)):
        if modulus(numbers[i]) == m:
            length+=1
        else:
            if length > maxlength:
                maxlength = length
                start_position = p
            length = 1
            p = i
            m = modulus(numbers[i])
    if length > maxlength:
        maxlength = length
        start_position = p
    if maxlength > 1:
        lst = []
        for i in range(start_position,start_position+maxlength):
            lst.append(numbers[i])
        return lst
    else:
        return None

def get_longest_sequence_difference_modulus_prime(numbers):
    '''
    Get the longest sequence of numbers with consecutive numbers
    having the difference between the modulus a prime number
    params:
        numbers - the list with all the numbers we have
    output
        None - if there isn't such a sequence
        the longerst sequence - otherwise
    '''
    maxlength = -1
    start_position = 0
    p = 0
    length = 1
    for i in range(1,len(numbers)):
        if isPrime(modulus(numbers[i-1])-modulus(numbers[i])):
            length+=1
        else:
            if length > maxlength:
                maxlength = length
                start_position = p
            length = 1
            p = i
    if length > maxlength:
        maxlength = length
        start_position = p
    if maxlength > 1:
        lst = []
        for i in range(start_position,start_position+maxlength):
            lst.append(numbers[i])
        return lst
    else:
        return None

def start():
    numbers = init_list_of_numbers()
    while True:
        print_menu()
        choice = input(">")
        if choice == "1":
            read_a_list_of_numbers(numbers)
        elif choice == "2":
            print("The list of numbers:")
            show_all_numbers(numbers)
        elif choice == "3":
            r = get_longest_sequence_same_modulus(numbers)
            if r == None:
                print("There isn't a sequence of numbers with the same modulus")
            else:
                print("This is the longest sequence of numbers with the same modulus:")
                show_all_numbers(r)
            r = get_longest_sequence_difference_modulus_prime(numbers)
            if r == None:
                print("There isn't a sequence of numbers with consecutive numbers having the difference between the modulus a prime number:")
            else:
                print("This is the longest sequence of numbers with consecutive numbers having the difference between the modulus a prime number:")
                show_all_numbers(r)

        elif choice == "4":
            return
        else:
            print("Invalid command")

start()
    
    
    
