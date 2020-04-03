class Driver:
    def __init__(self, did, name):
        self._driverId = did
        self.Name = name

    @property
    def driverId(self):
        return self._driverId

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    def __str__(self):
        return "driverId: " + str(self.driverId) + " name:" + self.Name


class Order:
    def __init__(self, did, dist):
        if dist < 1:
            raise ValueError("Not a valid distance")
        self._driverId = did
        self.Distance = dist

    @property
    def driverId(self):
        return  self._driverId

    @property
    def Distance(self):
        return self._distance

    @Distance.setter
    def Distance(self, value):
        self._distance = value

    def __str__(self):
        return "driverId: " + str(self._driverId) + " distance: " + str(self.Distance)