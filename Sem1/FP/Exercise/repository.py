from domain import *


class textRepository:
    def __init__(self, fileName):
        self._fileName = fileName
        self._students = self._load_file()

    def _load_file(self):
        data = []
        f = open(self._fileName, "r")
        line = f.readline().strip()
        while len(line) > 0:
            params = line.split(",")
            student = Student(int(params[0]), params[1], int(params[2]), int(params[3]))
            data.append(student)
            line = f.readline().strip()
        f.close()
        return data

    def get_students(self):
        return self._students

    def find_student_by_id(self, studentId):
        '''
        :param studentId: given student id
        :return: the student if found
                None otherwise
        '''
        for i in self._students:
            if i.studentId == studentId:
                return i
        return None

    def store_student(self, student):
        '''
        :param student: the student to be stored
        Store the student if unique id
        Raise an error otherwise
        '''
        if self.find_student_by_id(student.studentId) != None:
            raise ValueError("Id must be unique!")
        self._students.append(student)

    def update_student_grade(self, studentId, bonus):
        student = self.find_student_by_id(studentId)
        student.Grade += bonus
        if student.Grade > 10:
            student.Grade = 10
