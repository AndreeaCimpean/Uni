'''
    list of students
    menu-driven user
    student: id (string,unique), name, grade
    1.add a student
    2.delete one
    3.show all
    4.show, students with grades>than a given one
    5.exit
'''

#simple feature-driven development

#id = 114, name = "Anna", grade = 10
#how can we abstract the student's representaion from the program?

s = {"id":114,"name":'Anna',"grade":110} #as dict
#s = ['114','Anna',10] #as list
#s["name"]='Marie' #problem?

def create_student(sid = -1,sname = "n/a",sgrade = None):
    return {"id":sid,"name":sname,"grade":sgrade}

def set_student_id(student, sid):
    student["id"] = sid
def set_student_name(student, sname):
    student["name"] = sname
def set_student_id(student, sgrade):
    student["grade"] = sgrade

def get_student_id(student):
    return student["id"]
def get_student_name(student):
    return student["name"]
def get_student_grade(student):
    return student["grade"]

#set_student_name(s,'bla')
#print(get_student_name(s))
#print(s)

def show_students(students):
    print("List of students")
    for s in students:
        print("id: " + str(get_student_id(s)) + " name: " + get_student_name(s) + " grade: " + str(get_student_grade(s)))

def print_menu():
    print("1. Show the students")
    print("2. Add student")
    print("3. Delete student")
    print("4. Exit")

def init_students():
    res = []
    res.append(create_student(100,"Alice",10))
    res.append(create_student(101,"Bob",9))
    return res

def read_student():
    sid = int(input('student id='))
    sname = input('student name=')
    sgrade = int(input('student grade='))
    return create_student(sid,sname,sgrade)

def validate_student(student,studentList):
    '''
    Validates the given student
    params:
        student - given student
        studentList - list of registered students
    output
        None - student is valid
        error string - some error!? #error codes are nice, though
    '''
    for s in studentList:
        if get_student_id(student) == get_student_id(s):
            return "Duplicate student id"
    name=get_student_name(student)
    if len(name) == 0:
        return "Empty name"
    grade = get_student_grade(student)
    if grade < 1 or grade > 10:
        return "Invalid grade"
    return None

def add_student(studentList):
    #1. read student form console
    #2. validate student data (unique id, non-empty name, grade)
    #3. add student
    while True:
        student = read_student()
        msg=validate_student(student,studentList)
        if msg is not None:
            print(msg)
        else:
            studentList.append(student)
            return

def validate_student_id(sid,studentList):
    '''
    Validates the given student id
    params:
        sid - given student id
        studentList - list of registered students
    output
        True - student id is valid
        False - student does not exists
    '''
    for s in studentList:
        if get_student_id(s) == sid:
            return True
    return False

def show_student_details(sid,studentList):
    for s in studentList:
        if get_student_id(s) == sid:
            print("id: " + str(get_student_id(s)) + " name: " + get_student_name(s) + " grade: " + str(get_student_grade(s)))
            break
        
def delete_student(students):
    #1. read student id from console
    #2. validate student id
    #2. show student details
    #3. ask if sure
    #4. delete student
    #5. display a message
    sid=int(input('student id='))
    if(not validate_student_id(sid,students)):
        print('There is no student whith that id')
    else:
        show_student_details(sid,students)
        while True:
            print('Are you sure you want to delete this student? (Y/N)')
            answer = input('>')
            if(answer == "N"):
                return
            elif(answer == "Y"):
                for s in students:
                    if get_student_id(s) == sid:
                        students.remove(s)
                print('Student deleted')
                return
            else:
                print("Invalid command")

    
def start():
    #students = []
    students=init_students()
    while True:
        print_menu()
        choice = input(">")
        if choice == "1":
            show_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            return
        else:
            print("Invalid command")

start()
