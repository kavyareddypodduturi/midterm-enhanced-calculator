from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import HistoryManager
from app.calculator_memento import Caretaker
from app.input_validators import InputValidator
from app.logger import Logger
from app.calculator_config import CalculatorConfig
from app.exceptions import CalculatorError
from app.logger import LoggingObserver
from app.history import AutoSaveObserver
import pandas as pd
from app.exceptions import FileOperationError
from colorama import init, Fore, Style
init(autoreset=True)



class Calculator:
    """
    Core calculator logic integrating operations, history, memento, and logging.
    """

    def __init__(self):
        self.config = CalculatorConfig()
        self.history_manager = HistoryManager(self.config.max_history_size)
        self.history_manager.add_observer(LoggingObserver())
        self.history_manager.add_observer(AutoSaveObserver(self.history_manager))
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

    def save_history(self):
        try:
            data = [calc.to_dict() for calc in self.history_manager.get_all()]
            df = pd.DataFrame(data)
            df.to_csv(
                self.config.history_file,
                index=False,
                encoding=self.config.default_encoding,
            )
            self.logger.info("History manually saved.")
        except Exception as e:
            raise FileOperationError(f"Failed to save history: {e}")

    def load_history(self):
        try:
            df = pd.read_csv(
                self.config.history_file,
                encoding=self.config.default_encoding,
            )

            self.history_manager.clear()

            for _, row in df.iterrows():
                calculation = Calculation(
                    row["operation"],
                    float(row["operand1"]),
                    float(row["operand2"]),
                    float(row["result"]),
                )
                self.history_manager.add(calculation)

            self.logger.info("History loaded from file.")

        except FileNotFoundError:
            raise FileOperationError("History file not found.")
        except Exception as e:
            raise FileOperationError(f"Failed to load history: {e}")
        

if __name__ == "__main__":  # pragma: no cover
    calculator = Calculator()

    print(Fore.CYAN + "Enhanced Calculator (type 'help' for commands, 'exit' to quit)")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print(Fore.CYAN + "Exiting calculator.")
            break

        if user_input.lower() == "help":
            print(Fore.CYAN + "Available commands:")
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
            print(Fore.YELLOW + "History cleared.")
            continue

        if user_input.lower() == "undo":
            try:
                calculator.undo()
                print(Fore.YELLOW + "Undo successful.")
            except Exception as e:
                print(Fore.RED + str(e))
            continue

        if user_input.lower() == "redo":
            try:
                calculator.redo()
                print(Fore.YELLOW + "Redo successful.")
            except Exception as e:
                print(Fore.RED + str(e))
            continue

        if user_input.lower() == "save":
            try:
                calculator.save_history()
                print(Fore.YELLOW + "History saved manually.")
            except Exception as e:
                print(Fore.RED + str(e))
            continue

        if user_input.lower() == "load":
            try:
                calculator.load_history()
                print(Fore.YELLOW + "History loaded from file.")
            except Exception as e:
                print(Fore.RED + str(e))
            continue

        parts = user_input.split()

        if len(parts) == 3:
            operation_name, value1, value2 = parts
            try:
                result = calculator.perform_operation(
                    operation_name, value1, value2
                )
                print(Fore.GREEN + f"Result: {result}")
            except Exception as e:
                print(Fore.RED + str(e))
        else:
            print(Fore.RED + "Invalid command format. Use: operation value1 value2")        