import pytest

from Zadanie4 import Fibonacci_iteracyjnie, Fibonacci_rekurencyjnie

def test_fibonacci_iteracyjnie():
    assert Fibonacci_iteracyjnie(4) == 3
    assert Fibonacci_iteracyjnie(0) == 0
    assert Fibonacci_iteracyjnie(9) == 34
    with pytest.raises(TypeError):
        Fibonacci_iteracyjnie("7")
    with pytest.raises(ValueError):
        Fibonacci_iteracyjnie(-2)

def test_fibonacci_rekurencyjnie():
    assert Fibonacci_rekurencyjnie(4) == 3
    assert Fibonacci_rekurencyjnie(0) == 0
    assert Fibonacci_rekurencyjnie(9) == 34
    with pytest.raises(TypeError):
        Fibonacci_rekurencyjnie("7")
    with pytest.raises(ValueError):
        Fibonacci_rekurencyjnie(-2)