from app.exceptions import HistoryError


class HistoryManager:
    """
    Manages calculation history.
    """

    def __init__(self, max_size=100):
        self.history = []
        self.max_size = max_size

    def add(self, calculation):
        if len(self.history) >= self.max_size:
            self.history.pop(0)
        self.history.append(calculation)

    def clear(self):
        self.history.clear()

    def get_all(self):
        return self.history

    def get_last(self):
        if not self.history:
            raise HistoryError("No history available.")
        return self.history[-1]