import pytest
from atividades.src.atividade11_custom_sort import custom_sort

def test_custom_sort():
    assert custom_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    
def test_custom_sort_empty_list():
    assert custom_sort([]) == []
    
def test_custom_sort_negative_numbers():
    assert custom_sort([-5, -4, -3, -2, -1]) == [-1, -2, -3, -4, -5]
    
def test_custom_sort_mixed_numbers():
    assert custom_sort([-1, 2, -3, 4, -5]) == [4, 2, -1, -3, -5]
