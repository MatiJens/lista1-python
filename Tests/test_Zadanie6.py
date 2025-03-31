import pytest

from Zadanie6 import komplement, transkrybuj, transluj


def test_komplement():
    assert komplement(['A','T','C','C','G']) == ['C', 'G', 'G', 'A', 'T']
    with pytest.raises(ValueError):
        komplement(['A','U','C','C','G'])
    with pytest.raises(TypeError):
        komplement("GAGTCC")

def test_transkrybuj():
    assert transkrybuj(['C', 'G', 'G', 'A', 'T']) == ['A', 'U', 'C', 'C', 'G']
    with pytest.raises(ValueError):
        transkrybuj(['A','U','C','C','G'])
    with pytest.raises(TypeError):
        transkrybuj("GAGTCC")

def test_transluj():
    assert transluj(['A', 'U', 'G', 'A', 'U', 'C', 'U', 'A', 'C', 'U', 'A', 'C', 'U', 'A', 'A']) == ['Ile', 'Tyr', 'Tyr']
    assert transluj(['U', 'A', 'U', 'G', 'A', 'U', 'C', 'U', 'A', 'C', 'U', 'A', 'C', 'U', 'A', 'A']) == ['Ile', 'Tyr', 'Tyr']
    assert transluj(['U', 'U', 'A', 'U', 'G', 'A', 'U', 'C', 'U', 'A', 'C', 'U', 'A', 'C', 'U', 'A', 'A']) == ['Ile', 'Tyr', 'Tyr']
    assert transluj(['U', 'U', 'U', 'A', 'U', 'G', 'A', 'U', 'C', 'U', 'A', 'C', 'U', 'A', 'C', 'U', 'A', 'A']) == ['Ile', 'Tyr', 'Tyr']
    assert transluj(['A', 'G', 'G', 'A', 'U', 'C', 'U', 'A', 'C', 'U', 'A', 'C', 'U', 'A', 'A']) == "brak kodonu startu"
    assert transluj(['A', 'U', 'G', 'A', 'U', 'C', 'U', 'A', 'C', 'U', 'A', 'C', 'U', 'C', 'A']) == "brak kodonu stopu"
    with pytest.raises(ValueError):
        transluj(['A','T','C','C','G'])
    with pytest.raises(TypeError):
        transluj("AUGACUUAA")
