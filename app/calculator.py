from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import HistoryManager
from app.calculator_memento import Caretaker
from app.input_validators import InputValidator
from app.logger import Logger
from app.calculator_config import CalculatorConfig
from app.exceptions import CalculatorError
from app.logger import LoggingObserver


class Calculator:
    """
    Core calculator logic integrating operations, history, memento, and logging.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history_manager = HistoryManager(self.config.max_history_size)
        self.history_manager.add_observer(LoggingObserver())
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
            self.history_manager.add(calculation)

            # Save new state after adding calculation
            self.caretaker.save(self.history_manager.get_all())

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

if __name__ == "__main__":  # pragma: no cover
    calculator = Calculator()

    print("Enhanced Calculator (type 'help' for commands, 'exit' to quit)")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print("Exiting calculator.")
            break

        if user_input.lower() == "help":
            print("Available commands:")
            print("add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
            print("history, clear, undo, redo, exit")
            continue

        if user_input.lower() == "history":
            for item in calculator.get_history():
                print(
                    f"{item.operation} | {item.operand1}, {item.operand2} -> {item.result}"
                )
            continue

        if user_input.lower() == "clear":
            calculator.clear_history()
            print("History cleared.")
            continue

        if user_input.lower() == "undo":
            try:
                calculator.undo()
                print("Undo successful.")
            except Exception as e:
                print(e)
            continue

        if user_input.lower() == "redo":
            try:
                calculator.redo()
                print("Redo successful.")
            except Exception as e:
                print(e)
            continue

        parts = user_input.split()

        if len(parts) == 3:
            operation_name, value1, value2 = parts
            try:
                result = calculator.perform_operation(
                    operation_name, value1, value2
                )
                print(f"Result: {result}")
            except Exception as e:
                print(e)
        else:
            print("Invalid command format. Use: operation value1 value2")        