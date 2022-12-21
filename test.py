import pytest
from Rendimentos import Rendimento
from Deducoes import Deducoes

rendimento = [
    ('rendimento', 1),
    ('rendiment9', 2.9932),
    ('rend', 34123),
    (None, None),
    ('Teste', 34123)
]

deducao = [
    ('Previdencia', 362.4),
    ('dependentes', 600),
    (None, None),
]

@pytest.mark.parametrize(['descricao', 'valor'], rendimento)
def testRendimentoClass(descricao, valor):
    rendimento = Rendimento(descricao, valor)
    assert rendimento.valor == valor

@pytest.mark.parametrize(['descricao', 'valor'], rendimento)
def testRendimentoDescricaoInvalida(descricao, valor):
    rendimento = Rendimento(descricao, valor)
    assert rendimento.descricao == descricao

@pytest.mark.TesteFuncional
def testCalculaRendimento():
    rendimento = Rendimento('rendimento', 1)
    assert rendimento.CalculaRendimento() == 1

# DEDUÇOES

@pytest.mark.parametrize(['descricao', 'valor'], deducao)
def testDeducaoClass(descricao, valor):
    deducao = Deducoes(descricao, valor)
    assert deducao.valorDeducao == valor

def testDeducaoDescricaoInvalida():
    deducao = Deducoes('Previdencia', 362.4)
    assert deducao.deducao == 'Previdencia'


