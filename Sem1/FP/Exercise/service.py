from domain import *

class Service:
    def __init__(self, repo):
        self._repository = repo

    def get_students(self):
        return self._repository.get_students()

    def add_student(self, studentId, name, attendance, grade):
        '''
        :param studentId: the given id
        :param name: the given name
        :param attendance: the given attendance count
        :param grade: the given grade
        Call repository function to store the new student, if valid student
        An error catched by the ui ocurres otherwise
        '''
        student = Student(studentId, name, attendance, grade)
        self._repository.store_student(student)

    def give_bonus(self, p,b):
        for i in self.get_students():
            if i.Attendance >= p:
                self._repository.update_student_grade(i.studentId,b)

    def search_student_by_name(self, substring):
        students = []
        for i in self.get_students():
            if substring.lower() in i.Name.lower():
                students.append(i)
        students = self.sort_by_name(students)
        return students

    def sort_by_name(self, students):
        for i in range(0, len(students)-1):
            for j in range(i+1,len(students)):
                if students[i].Name > students[j].Name:
                    aux = students[i]
                    students[i] = students[j]
                    students[j] = aux
        return students