import pytest
from Rendimentos import Rendimento
from Exceptions_test import test_exception

rendimento = [
    ('rendimento', 1),
    ('rendiment9', 2),
    ('rend', 34123),
    (None, None),
    ('rendimento', 34123)
]

@pytest.mark.parametrize(['descricao', 'valor'], rendimento)
def test_rendimento_class(descricao, valor):
    rendimento = Rendimento(descricao, valor)
    assert rendimento.valor == valor

@pytest.mark.parametrize(['descricao', 'valor'], rendimento)
def test_rendimento_class_invalid_description(descricao, valor):
    rendimento = Rendimento(descricao, valor)
    assert rendimento.descricao == descricao

@pytest.mark.TesteFuncional
def testCalculaRendimento():
    rendimento = Rendimento('rendimento', 1)
    assert rendimento.CalculaRendimento() == 1



