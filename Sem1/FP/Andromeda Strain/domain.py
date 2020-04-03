class Person:
    def __init__(self, id, immun, status, days):
        self._id = id
        self.Immunization = immun
        self.Status = status
        self.DaysIll = days

    @property
    def id(self):
        return self._id

    @property
    def Immunization(self):
        return self._immunization

    @Immunization.setter
    def Immunization(self, value):
        self._immunization = value

    @property
    def Status(self):
        return self._status

    @Status.setter
    def Status(self, value):
        self._status = value

    @property
    def DaysIll(self):
        return self._days_ill

    @DaysIll.setter
    def DaysIll(self, value):
        self._days_ill = value

    def __str__(self):
        return "id: " + str(self.id) + " immunization: " + self.Immunization + " status: " + self.Status + " days ill: " + str(self.DaysIll)