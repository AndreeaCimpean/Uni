class UndoService:
    def __init__(self):
        self._history = []
        self._index = 0
        self._duringUndoRedo = False

    def recordOperation(self, operation):
        if self._duringUndoRedo == True:
            return

        if self._index < len(self._history):
            self._history = self._history[:self._index]

        self._history.append(operation)
        self._index += 1

    def undo(self):
        if self._index == 0:
            raise ValueError("No more undos!")
        self._duringUndoRedo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndoRedo = False

    def redo(self):
        if self._index == len(self._history):
            raise ValueError("No more redos!")
        self._duringUndoRedo = True
        self._history[self._index].redo()
        self._index += 1
        self._duringUndoRedo = False


class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._parameters = parameters

    def call(self):
        self._function(*self._parameters)


class Operation:
    def __init__(self, undofunction, redofunction):
        self._undo = undofunction
        self._redo = redofunction

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()


class CascadeOperation:
    def __init__(self, listOperations):
        self._listOperations = listOperations

    def undo(self):
        for op in self._listOperations:
            op.undo()

    def redo(self):
        for op in self._listOperations:
            op.redo()