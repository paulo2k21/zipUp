import pytest
from atividades.src.atividade08_average import calculate_average

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5, 6, 7]) == 4.0
    assert calculate_average([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5
    assert calculate_average([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5.0
    assert calculate_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5

def test_calculate_average_empty_list():
    with pytest.raises(ValueError) as error:
        calculate_average([])
    assert str(error.value) == "The list of numbers cannot be empty"

def test_calculate_average_negative_numbers():
    assert calculate_average([-1, -2, -3, -4, -5, -6, -7]) == -4.0
    assert calculate_average([-1, -2, -3, -4, -5, -6, -7, -8]) == -4.5
    assert calculate_average([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == -5.0
    assert calculate_average([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -5.5

def test_calculate_average_mixed_numbers():
    assert calculate_average([-1, 2, -3, 4, -5]) == -0.6
    assert calculate_average([-1, 2, -3, 4, -5, 6, -7, 8]) == 0.5

def test_calculate_average_float_numbers():
    assert calculate_average([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]) == 4.4
    assert calculate_average([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]) == 4.95

def test_calculate_average_mixed_float_numbers():
    assert calculate_average([-1.1, 2.2, -3, 4.4, -5.5, 6, 4]) == 1.0
    assert calculate_average([-1.1, 2.2, -3.3, 4.4, -5.5, 6.6, -7.7, 8.8]) == 0.55