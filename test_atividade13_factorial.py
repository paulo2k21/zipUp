import pytest
from atividades.src.atividade13_factorial import factorial

def test_factorial_negative_number():
    with pytest.raises(ValueError) as error:
        factorial(-10)
    assert str(error.value) == "n must be a non-negative integer"
    
def test_factorial_zero():
    assert factorial(0) == 1
    
def test_factorial_positive_number():
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000