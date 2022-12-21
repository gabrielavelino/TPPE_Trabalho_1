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
    assert deducao.valor == valor

def testDeducaoDescricaoInvalida():
    deducao = Deducoes('Previdencia', 362.4)
    assert deducao.deducao == 'Previdencia'

def testCalculoDeducao():
    deducao = Deducoes('Previdencia', 362.4)
    assert deducao.CalculaDeducoes([362.4]) == 362.4

def testCalculoDeducaoInt():
    deducao = Deducoes('Previdencia', 362.4)
    listaTeste = [300,300,150,150,100]
    assert deducao.CalculaDeducoes(listaTeste) == 1000

def testCalculoDeducaoFloat():
    deducao = Deducoes('Previdencia', 362.4)
    listaTeste = [25.5,25.25]
    assert deducao.CalculaDeducoes(listaTeste) == 50.75

def testCalculoDeducaoFloat():
    deducao = Deducoes('Previdencia', 1)
    listaTeste = [100,120.5,10.3,2.2]
    assert deducao.CalculaDeducoes(listaTeste) == 233.0

# # EXCEÇOES
# @pytest.mark.TesteExcecao
# def testDescricaoEmBrancoOutrasDeducoes():
#         with pytest.raises(DescricaoEmBrancoException):
#             deducao = Deducoes('', 0)



