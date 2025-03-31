import pytest

from Zadanie2 import wspolne


def test_wspolne():
    assert wspolne([1,2,3,4,5],[2,4,6,8]) == [2,4]
    assert wspolne([1, 1, 1, 1], [1, 1, 1, 2]) == [1,1,1]
    assert wspolne([1,2,3],[4,5,6]) == []
    with pytest.raises(TypeError):
        wspolne([1,2,3,4],2)
