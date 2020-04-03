class BookException(Exception):
    def __init__(self,message):
        super().__init__(message)

class ClientException(Exception):
    def __init__(self,message):
        super().__init__(message)

class RentalException(Exception):
    def __init__(self,message):
        super().__init__(message)