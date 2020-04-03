class Settings:
    def __init__(self, filename):
        self._fileName = filename
        self.RepositoryType = ""
        self.MoviesFile = ""
        self.ClientsFile = ""
        self.RentalsFile = ""
        self._load_settings_file()

    @property
    def RepositoryType(self):
        return self._repository_type

    @RepositoryType.setter
    def RepositoryType(self, value):
        self._repository_type = value

    @property
    def MoviesFile(self):
        return self._movies_file

    @MoviesFile.setter
    def MoviesFile(self, value):
        self._movies_file = value

    @property
    def ClientsFile(self):
        return self._clients_file

    @ClientsFile.setter
    def ClientsFile(self, value):
        self._clients_file = value

    @property
    def RentalsFile(self):
        return self._rentals_file

    @RentalsFile.setter
    def RentalsFile(self, value):
        self._rentals_file = value

    def _load_settings_file(self):
        f = open(self._fileName, 'r')
        line = f.readline().strip()
        repositoryType = line[line.find("= ") + 2:]

        line = f.readline().strip()
        moviesFile = line[line.find("= ") + 3:]
        moviesFile = moviesFile[:len(moviesFile) - 1]

        line = f.readline().strip()
        clientsFile = line[line.find("= ") + 3:]
        clientsFile = clientsFile[:len(clientsFile) - 1]

        line = f.readline().strip()
        rentalsFile = line[line.find("= ") + 3:]
        rentalsFile = rentalsFile[:len(rentalsFile) - 1]
        f.close()

        self.RepositoryType = repositoryType
        self.MoviesFile = moviesFile
        self.ClientsFile = clientsFile
        self.RentalsFile = rentalsFile
