class RepositoryException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Repository:
    def __init__(self):
        self._objects = []

    def store(self, object):
        for o in self._objects:
            if o.Id == object.Id:
                raise RepositoryException("Id must be unique")
        self._objects.append(object)

    def __len__(self):
        return len(self._objects)

    def __getitem__(self, index):
        return self._objects[index]

    def find(self, objectId):
        for i in range(0, len(self._objects)):
            if self._objects[i].Id == objectId:
                return i
        raise RepositoryException("Id is not in the list")

    def delete(self, objectId):
        for o in self._objects:
            if o.Id == objectId:
                self._objects.remove(o)

