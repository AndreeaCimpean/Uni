from service import *
from repository import *

class UI:
    def __init__(self, serv):
        self._service = serv

    def read_command(self):
        command = input("your command: ")
        idx = command.find(" ")
        if idx == -1:
            return(command,[])
        cmd = command[:idx]
        params = command[idx+1:].split(",")
        return (cmd,params)

    def start(self):
        commandList = {"add":self.add_student, "list":self.show_all_students, "display":self.display_students_name, "bonus":self.give_bonus}
        while True:
            command = self.read_command()
            cmd = command[0]
            params = command[1]
            if cmd == "exit":
                return
            else:
                commandList[cmd](params)

    def add_student(self, params):
        studentId = int(params[0])
        name = params[1]
        attendance = int(params[2])
        grade = int(params[3])
        try:
            self._service.add_student(studentId, name, attendance, grade)
        except ValueError as ve:
            print(ve)

    def show_all_students(self, params):
        for i in self._service.get_students():
            print(i)

    def give_bonus(self, params):
        self._service.give_bonus(int(params[0]), int(params[1]))

    def display_students_name(self, params):
        for i in self._service.search_student_by_name(params[0]):
            print(i)


repo = textRepository("input.txt")
serv = Service(repo)
ui = UI(serv)
ui.start()