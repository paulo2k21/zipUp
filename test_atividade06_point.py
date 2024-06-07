import pytest
from atividades.src.atividade06_point import Point

def test_distance_to_with_positive_numbers():
    p1 = Point(1, 1)
    p2 = Point(4, 5)
    assert p1.distance_to(p2) == 5.0

def test_distance_to_with_negative_numbers():
    p1 = Point(-1, -1)
    p2 = Point(-4, -5)
    assert p1.distance_to(p2) == 5.0

def test_distance_to_with_mixed_numbers():
    p1 = Point(-1, 1)
    p2 = Point(4, -5)
    assert p1.distance_to(p2) == 7.810249675906654

def test_distance_to_with_zero():
    p1 = Point(10, 5)
    p2 = Point(0, 0)
    assert p1.distance_to(p2) == 11.180339887498949

def test_distance_to_with_invalid_argument():
    p1 = Point(1, 1)
    with pytest.raises(ValueError) as error:
        p1.distance_to(1)
    assert str(error.value) == "Argument must be a Point"