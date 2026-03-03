from app.exceptions import HistoryError


class HistoryManager:
    """
    Manages calculation history and notifies observers.
    """

    def __init__(self, max_size=100):
        self.history = []
        self.max_size = max_size
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self._observers:
            observer.update(calculation)

    def add(self, calculation):
        if len(self.history) >= self.max_size:
            self.history.pop(0)

        self.history.append(calculation)
        self.notify_observers(calculation)

    def clear(self):
        self.history.clear()

    def get_all(self):
        return self.history

    def get_last(self):
        if not self.history:
            raise HistoryError("No history available.")
        return self.history[-1]
    
import pandas as pd
from app.calculator_config import CalculatorConfig
from app.exceptions import FileOperationError


class AutoSaveObserver:
    """
    Observer that automatically saves calculation history to CSV.
    """

    def __init__(self, history_manager):
        self.history_manager = history_manager
        self.config = CalculatorConfig()

    def update(self, calculation):
        if not self.config.auto_save:
            return

        try:
            data = [
                calc.to_dict() for calc in self.history_manager.get_all()
            ]

            df = pd.DataFrame(data)

            df.to_csv(
                self.config.history_file,
                index=False,
                encoding=self.config.default_encoding,
            )

        except Exception as e:
            raise FileOperationError(f"Failed to auto-save history: {e}")    