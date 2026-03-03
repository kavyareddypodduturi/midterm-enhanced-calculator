from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import HistoryManager
from app.calculator_memento import Caretaker
from app.input_validators import InputValidator
from app.logger import Logger
from app.calculator_config import CalculatorConfig
from app.exceptions import CalculatorError


class Calculator:
    """
    Core calculator logic integrating operations, history, memento, and logging.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history_manager = HistoryManager(self.config.max_history_size)
        self.caretaker = Caretaker()
        self.validator = InputValidator()
        self.logger = Logger.get_logger()

    def perform_operation(self, operation_name, value1, value2):
        try:
            a, b = self.validator.validate_two_numbers(value1, value2)

            operation = OperationFactory.create_operation(operation_name)
            result = operation.execute(a, b)

            # Round according to precision setting
            result = round(result, self.config.precision)

            calculation = Calculation(operation_name, a, b, result)

            # Save current state for undo
            self.caretaker.save(self.history_manager.get_all())

            self.history_manager.add(calculation)

            self.logger.info(
                f"{operation_name} | {a}, {b} -> {result}"
            )

            return result

        except CalculatorError as e:
            self.logger.error(str(e))
            raise

    def get_history(self):
        return self.history_manager.get_all()

    def clear_history(self):
        self.history_manager.clear()
        self.logger.info("History cleared.")

    def undo(self):
        state = self.caretaker.undo()
        self.history_manager.history = state
        self.logger.info("Undo performed.")

    def redo(self):
        state = self.caretaker.redo()
        self.history_manager.history = state
        self.logger.info("Redo performed.")