class Service:
    def __init__(self,movies,clients):
        self._listMovies = movies
        self._listClients = clients

    @property
    def listMovies(self):
        return self._listMovies

    @property
    def listClients(self):
        return self._listClients