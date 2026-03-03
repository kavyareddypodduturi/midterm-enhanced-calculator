import math
from app.exceptions import OperationError


class Operation:
    """
    Base class for all operations.
    """

    def execute(self, a, b):
        raise NotImplementedError("Execute method must be implemented.")


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero is not allowed.")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Root degree cannot be zero.")
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of a negative number is not allowed.")
        return a ** (1 / b)


class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Modulus by zero is not allowed.")
        return a % b


class IntegerDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Integer division by zero is not allowed.")
        return a // b


class Percent(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate percentage with divisor zero.")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    def execute(self, a, b):
        return abs(a - b)


class OperationFactory:
    """
    Factory class to create operation instances.
    """

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntegerDivide,
        "percent": Percent,
        "abs_diff": AbsoluteDifference,
    }

    @classmethod
    def create_operation(cls, operation_name):
        operation_name = operation_name.lower()
        if operation_name not in cls.operations:
            raise OperationError(f"Unsupported operation: {operation_name}")
        return cls.operations[operation_name]()