from app.exceptions import HistoryError


class Memento:
    """
    Stores a snapshot of calculator history state.
    """

    def __init__(self, state):
        self._state = list(state)

    def get_state(self):
        return list(self._state)


class Caretaker:
    """
    Manages undo and redo stacks.
    """

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            raise HistoryError("Nothing to undo.")

        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)
        return memento.get_state()

    def redo(self):
        if not self._redo_stack:
            raise HistoryError("Nothing to redo.")

        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        return memento.get_state()