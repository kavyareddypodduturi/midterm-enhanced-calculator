import pytest
from app.calculator import Calculator
from app.exceptions import ValidationError, OperationError


def test_perform_add():
    calc = Calculator()
    result = calc.perform_operation("add", 5, 5)
    assert result == 10.0


def test_history_after_operation():
    calc = Calculator()
    calc.perform_operation("add", 2, 3)
    history = calc.get_history()
    assert len(history) == 1
    assert history[0].result == 5.0


def test_undo_functionality():
    calc = Calculator()
    calc.perform_operation("add", 10, 5)
    calc.perform_operation("add", 2, 3)
    calc.undo()
    history = calc.get_history()
    assert len(history) == 1
    assert history[0].result == 15.0


def test_redo_functionality():
    calc = Calculator()
    calc.perform_operation("add", 10, 5)
    calc.perform_operation("add", 2, 3)
    calc.undo()
    calc.redo()
    history = calc.get_history()
    assert len(history) == 2
    assert history[1].result == 5.0


def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(OperationError):
        calc.perform_operation("invalid", 1, 2)


def test_invalid_input():
    calc = Calculator()
    with pytest.raises(ValidationError):
        calc.perform_operation("add", "abc", 2)