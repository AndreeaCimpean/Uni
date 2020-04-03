class Route:
    def __init__(self, rid, length):
        self._routeId = rid
        self.Length = length

    @property
    def routeId(self):
        return self._routeId

    @property
    def Length(self):
        return self._length

    @Length.setter
    def Length(self, value):
        self._length = value

    def __str__(self):
        return 'routeId: ' + str(self.routeId) + ' , '+ str(self.Length) + ' km'


class Bus:
    def __init__(self, bid, rcode, model, times):
        self._busId = bid
        self.routeCode = rcode
        self.Model = model
        self.Times = times

    @property
    def busId(self):
        return self._busId

    @property
    def routeCode(self):
        return self._routeCode

    @routeCode.setter
    def routeCode(self, value):
        self._routeCode = value

    @property
    def Model(self):
        return self._model

    @Model.setter
    def Model(self, value):
        self._model = value

    @property
    def Times(self):
        return self._times

    @Times.setter
    def Times(self, value):
        self._times = value

    def __str__(self):
        return 'id: ' + str(self.busId) + ' route code: ' + str(self.routeCode) + ' model: ' + self.Model + 'times on route: ' + str(self.Times)