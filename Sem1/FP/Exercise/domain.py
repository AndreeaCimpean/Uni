class Student:
    def __init__(self, sid, name, attendance, grade):
        if name.find(" ") == -1 or len(name[:name.find(" ")]) < 3 or len(name[name.find(" ")+1:]) <3:
            raise ValueError("Invalid Name")
        if attendance <= 0:
            raise ValueError("Invalid attendance count")
        if grade < 0 or grade > 10:
            raise ValueError("Invalid grade")
        self._studentId = sid
        self.Name = name
        self.Attendance = attendance
        self.Grade = grade

    @property
    def studentId(self):
        return self._studentId

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def Attendance(self):
        return self._attendance

    @Attendance.setter
    def Attendance(self, value):
        self._attendance = value

    @property
    def Grade(self):
        return self._grade

    @Grade.setter
    def Grade(self, value):
        self._grade = value

    def __str__(self):
        return "id: " + str(self.studentId) + " name: " + self.Name + " attendance count: " + str(self.Attendance) + " grade: " +str(self.Grade)


