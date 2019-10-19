#command-driven UI
#function specification
#tests
#VS Code, Eclipse + PyDev, PyCharm, Visual Studio,...

#command_word <param1,param2>
#add <student id>, <name>, <grade>
#delete <student id>
#list
#help!
#exit

#e.g. add 123,Popescu Elena,9
#   add 123,  Popescu Elena -> programs screams ERROR
#   delete 123
#   delete 21 -> ERROR

#feature-driven development

def create_student(sid,name,grade): #not UI
    '''
    Create a student
    params:
        sid - id
        name - string of len >3
        grade - int between 1 an 10
    output:
        success - return the student
        error - None
    '''
    if len(name) < 3:
        return None
    grade = int(grade)
    if grade < 1 or grade > 10:
        return None
    return [sid,name,grade]
        
def get_id(student):    
    return student[0]
def get_name(student):
    return student[1]
def get_grade(student):
    return student[2]

def find_student(studentList,sid):
    '''
    Find student having given id
    params: ...
    output:
        Student having given id
        None, student with given id not in list
    '''
    for s in studentList:
        if get_id(s):
            #this is the student youa are looking for
            return s
    return None

#function signature - uniquely identifies the function (function name, input params, return type)
def add_student(studentList, student):
    '''
    Specifications tell WHAT, not HOW
    Add student to list
    pamas:
        student - the list of students
        student - the student
    output:
        0 - success
        1 - Duplicate student id
    '''
    if find_student(studentList, get_id(student)) != None:
        return 1
    studentList.append(student)
    return 0

#1. function signature
#2. specification
#3. we can write a test for it

def readCommand():
    '''
    Read and parse the user's command
    '''
    #add 123,Popescu Elena,9
    cmd = input("command: ")
    #cmd = 'add 123,Popescu Elena,9'
    #1. Separate the command word form the params
    #2. Identify params
    #3. Return tuple(sommand,list of params)
    idx = cmd.find(" ")
    if idx == -1:
        return(cmd,[])
    command = cmd[:idx]
    params = cmd[idx:]
    params = params.split(",")

    for i in range(len(params)):
        params[i] = params[i].strip()
    
    #print(command)
    #print(params)
    return (command,params)

def add_student_UI(studentList, params):
    if len(params) != 3:
        print("Bad student parameters")
        return
    s = create_student(params[0],params[1],params[2])
    if s == None:
        print("Invalid student data")
        return
    if add_student(studentList,s) == 1:
        print("Duplicate student id!")

def start():
    studentList=[]
    while True:
        #read user command
        print(studentList)
        cmdtuple = readCommand()
        cmd = cmdtuple[0]
        params = cmdtuple[1]
        if cmd == 'add':
            add_student_UI(studentList,params)
        elif cmd == 'exit':
            break
        else:
            print("Bad command")

start()

#What do test functions do?
#1. Take no parameters -> we want them to have no context
#2. They have no user input/output
#3. If the code is correct, do nothing visible
#4. If the code has an error > SCREAM 
def test_add_student():
    slist = []
    s1 = create_student(1,"Marie",10)
    add_student(slist,s1)
    assert add_student(slist,s1) == 0
    assert len(slist) == 1
    assert get_id(slist[0]) == 1
    
    assert add_student(s1) == 1
    assert len(slist) == 1
    #assert <expression>


x=test_add_student
x() #dunction call operator
