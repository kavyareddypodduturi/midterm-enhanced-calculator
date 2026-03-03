class CalculatorError(Exception):
    """Base class for calculator-related errors."""
    pass


class OperationError(CalculatorError):
    """Raised when an invalid operation occurs."""
    pass


class ValidationError(CalculatorError):
    """Raised when input validation fails."""
    pass


class HistoryError(CalculatorError):
    """Raised when history operations fail (undo/redo issues)."""
    pass


class FileOperationError(CalculatorError):
    """Raised when file read/write operations fail."""
    pass


class ConfigurationError(CalculatorError):
    """Raised when configuration settings are invalid."""
    pass