import pytest

from zadanie1 import heron


def test_heron():
    assert round(heron(2, 2, 2),2) == 1.73
    assert round(heron(2, 1, 2),2) == 0.97
    with pytest.raises(ValueError):
        heron(2,1,20)
    with pytest.raises(TypeError):
        heron(2, "1", 20)
