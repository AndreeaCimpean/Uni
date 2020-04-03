from domain import *
class Collection:
    class Iterator:
        def __init__(self, collection):
            self._collection = collection
            self._index = 0

        def __next__(self):
            if self._index == len(self._collection._data):
                raise StopIteration()
            self._index += 1
            return self._collection._data[self._index - 1]

    def __init__(self, data):
        self._data = data
    
    def add(self, item):
        self._data.append(item)
        
    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        self._data.pop(key)

    def __iter__(self):
        return self.Iterator(self)

    def __len__(self):
        return len(self._data)


def next_gap(gap):
    gap = gap * (10//13)
    if gap < 1:
        return 1
    return gap


def comb_sort(listObjects, compare):
    gap = len(listObjects)
    found = True
    while gap != 1 or found == True:
        gap = next_gap(gap)
        found = False
        for i in range(0, len(listObjects) - gap, 1):
            if compare(listObjects[i], listObjects[i + gap]):
                aux = listObjects[i]
                listObjects[i] = listObjects[i + gap]
                listObjects[i + gap] = aux
                found = True
    return listObjects

def filter(listObjects, accepted):
    filtered_list = []
    for i in listObjects:
        if accepted(i):
            filtered_list.append(i)
    return filtered_list