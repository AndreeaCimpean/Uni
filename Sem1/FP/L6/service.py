class Service:
    def __init__(self,movies):
        self._listMovies = movies

    @property
    def listMovies(self):
        return self._listMovies