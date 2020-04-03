class MovieException(Exception):

    def __init__(self, message):
        super().__init__(message)


class ClientException(Exception):

    def __init__(self, message):
        super().__init__(message)


class RentalException(Exception):

    def __init__(self, message):
        super().__init__(message)


class RepositoryException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidatorException(Exception):
    def __init__(self, messageList=["Validation error!"]):
        self._messageList = messageList

    def getMessage(self):
        return self._messageList

    def __str__(self):
        result =""
        for message in self.getMessage():
            result += message
            result += '\n'
        return result