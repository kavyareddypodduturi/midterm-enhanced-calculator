from datetime import datetime


class Calculation:
    """
    Represents a single calculation entry.
    """

    def __init__(self, operation, operand1, operand2, result):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }