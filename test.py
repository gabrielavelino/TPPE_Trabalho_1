import pytest
from Rendimentos import Rendimento
from Deducoes import Deducoes
from Exceptions_test import ValorRendimentoInvalidoException, DescricaoEmBrancoException, ValorDeducaoInvalidoException, NomeEmBrancoException

rendimento = [
    ('rendimento', 1),
    ('rendiment9', 2.9932),
    ('rend', 34123),
    ('Teste', 34123),
]

rendimentoDescricao = [
    ('rendimento',1),
]

rendimentoInvalido = [
    (None, None),
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

@pytest.mark.parametrize(['descricao', 'valor'], rendimentoDescricao)
def testRendimentoDescricaoValida(descricao, valor):
    rendimento = Rendimento(descricao, valor)
    assert rendimento.getDescricao() == descricao

@pytest.mark.parametrize(['descricao','valor'], rendimentoInvalido)
def testRendimentoDescricaoInvalida(descricao, valor):
    rendimento = Rendimento(descricao, valor)
    rendimento.setDescricao('Nao pode ser nulo')
    assert not rendimento.getDescricao() == descricao

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

def testCalculoDeducao():
    deducao = Deducoes('Previdencia', 362.4)
    assert deducao.CalculaDeducoes([362.4]) == 362.4
    
@pytest.mark.TesteExcecao
def testDescricaoEmBrancoOutrasDeducoes():
        deducao = Deducoes()
        with pytest.raises(DescricaoEmBrancoException):
            deducao.setDeducao("")



