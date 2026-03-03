from app.exceptions import ValidationError
from app.calculator_config import CalculatorConfig


class InputValidator:
    """
    Handles validation of user inputs.
    """

    def __init__(self):
        self.config = CalculatorConfig()

    def validate_number(self, value):
        try:
            number = float(value)
        except ValueError:
            raise ValidationError("Input must be a numeric value.")

        if abs(number) > self.config.max_input_value:
            raise ValidationError(
                f"Input exceeds maximum allowed value ({self.config.max_input_value})."
            )

        return number

    def validate_two_numbers(self, value1, value2):
        num1 = self.validate_number(value1)
        num2 = self.validate_number(value2)
        return num1, num2