import os
import pytest
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.exceptions import FileOperationError


def test_manual_save_and_load(tmp_path):
    calc = Calculator()

    # Override history file location for safe testing
    config = CalculatorConfig()
    config.history_file = os.path.join(tmp_path, "test_history.csv")
    calc.config.history_file = config.history_file

    calc.perform_operation("add", 4, 6)
    calc.save_history()

    # Clear and reload
    calc.clear_history()
    assert len(calc.get_history()) == 0

    calc.load_history()
    assert len(calc.get_history()) == 1
    assert calc.get_history()[0].result == 10.0


def test_load_file_not_found(tmp_path):
    calc = Calculator()
    calc.config.history_file = os.path.join(tmp_path, "non_existent.csv")

    with pytest.raises(FileOperationError):
        calc.load_history()


def test_config_defaults():
    config = CalculatorConfig()
    assert config.max_history_size > 0
    assert config.precision >= 0
    assert config.max_input_value > 0