import pytest

from Zadanie5 import collatz


def test_collatz():
    assert collatz(6) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(11) == [34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    with pytest.raises(ValueError):
        collatz(-3)
    with pytest.raises(TypeError):
        collatz("88")
