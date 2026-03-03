import os
from dotenv import load_dotenv


class CalculatorConfig:
    """
    Loads and manages configuration settings for the calculator application.
    """

    def __init__(self):
        load_dotenv()

        self.log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "history")
        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE", "history/calculation_history.csv"
        )
        self.max_history_size = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
        self.auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        self.precision = int(os.getenv("CALCULATOR_PRECISION", 4))
        self.max_input_value = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1000000))
        self.default_encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
        self.log_file = os.getenv("CALCULATOR_LOG_FILE", "logs/calculator.log")

        self._validate_config()
        self._create_directories()

    def _validate_config(self):
        if self.max_history_size <= 0:
            raise ValueError("CALCULATOR_MAX_HISTORY_SIZE must be greater than 0.")

        if self.precision < 0:
            raise ValueError("CALCULATOR_PRECISION cannot be negative.")

        if self.max_input_value <= 0:
            raise ValueError("CALCULATOR_MAX_INPUT_VALUE must be positive.")

    def _create_directories(self):
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.history_dir, exist_ok=True)