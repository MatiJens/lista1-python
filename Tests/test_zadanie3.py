import pytest

from zadanie3 import podzbiory


def test_podzbiory():
    assert podzbiory({1,2,3}) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert podzbiory({2,2}) == [[], [2]]
    assert podzbiory(set()) == [[]]
    with pytest.raises(TypeError):
        podzbiory([1,2,3,4])
