import pytest
from app.operations import OperationFactory


def test_add_operation():
    operation = OperationFactory.create_operation("add")
    assert operation.execute(5, 3) == 8


def test_divide_operation():
    operation = OperationFactory.create_operation("divide")
    assert operation.execute(10, 2) == 5


def test_divide_by_zero():
    operation = OperationFactory.create_operation("divide")
    with pytest.raises(Exception):
        operation.execute(10, 0)


@pytest.mark.parametrize(
    "operation_name,a,b,expected",
    [
        ("subtract", 10, 5, 5),
        ("multiply", 4, 3, 12),
        ("power", 2, 3, 8),
        ("modulus", 10, 3, 1),
        ("int_divide", 10, 3, 3),
        ("percent", 50, 200, 25),
        ("abs_diff", 10, 20, 10),
    ],
)
def test_multiple_operations(operation_name, a, b, expected):
    operation = OperationFactory.create_operation(operation_name)
    assert operation.execute(a, b) == expected