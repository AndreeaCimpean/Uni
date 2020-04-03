import unittest
from service import *
from repository import *

class TestFirst(unittest.TestCase):
    def test_find_student_by_id(self):
        repo = textRepository("input.txt")
        s = repo.get_students()[0]
        self.assertEqual(repo.find_student_by_id(s.studentId),s)
        self.assertEqual(repo.find_student_by_id(1000000),None)

    def test_add_student(self):
        repo = textRepository("input.txt")
        serv = Service(repo)
        s = Student(1,"Mara Ioana",12,3)
        serv.add_student(1, "Mara Ioana", 12, 3)

        newstudent = serv.get_students()[len(serv.get_students())-1]

        self.assertEqual(s.studentId, newstudent.studentId)
        self.assertEqual(s.Name, newstudent.Name)
        self.assertEqual(s.Attendance, newstudent.Attendance)
        self.assertEqual(s.Grade, newstudent.Grade)

        with self.assertRaises(ValueError):
            serv.add_student(1,"Mara Ioana", 12, 3)
        with self.assertRaises(ValueError):
            serv.add_student(2,"Elena Daria", -12, 3)