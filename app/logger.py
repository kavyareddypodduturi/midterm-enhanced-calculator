import logging
import os
from app.calculator_config import CalculatorConfig


class Logger:
    """
    Centralized Logger configuration for the calculator application.
    """

    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            config = CalculatorConfig()

            logger = logging.getLogger("CalculatorLogger")
            logger.setLevel(logging.INFO)

            if not logger.handlers:
                file_handler = logging.FileHandler(
                    config.log_file, encoding=config.default_encoding
                )
                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

            cls._logger = logger

        return cls._logger
    
class LoggingObserver:
    """
    Observer that logs each new calculation.
    """

    def __init__(self):
        self.logger = Logger.get_logger()

    def update(self, calculation):
        self.logger.info(
            f"New Calculation Logged | "
            f"{calculation.operation} | "
            f"{calculation.operand1}, {calculation.operand2} -> {calculation.result}"
        )    