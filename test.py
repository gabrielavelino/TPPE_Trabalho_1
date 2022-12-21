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
    (500),
    (600),
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


def testDeducaoClass():
    deducao = Deducoes()
    deducao.cadastrarPrevidenciaOficial('Teste',500)
    deducao.cadastrarDeducao('Test2',500)
    valor = 1000

    assert deducao.CalculaDeducoes() == valor

def testDeducaoDependentes():
    deducao = Deducoes()
    deducao.cadastrarPrevidenciaOficial('Teste',500)
    deducao.cadastrarDeducao('Test2',500)
    valor = 1000

    assert deducao.CalculaDeducoes() == valor

def testCadastroTotalDeducoes():
    deducao = Deducoes()
    deducao.cadastrarPensaoAlimenticia('Filho',300)
    deducao.cadastrarDeducao('Teste',250)
    deducao.cadastrarPrevidenciaOficial('renda',250)
    deducao.cadastrarDependentes('Bonifacio','08/08/1998') # 1 dependente = 189,55
    valor = 989.55

    assert deducao.CalculaDeducoes() == valor

    
# @pytest.mark.TesteExcecao
# def testDescricaoEmBrancoOutrasDeducoes():
#         deducao = Deducoes()
#         with pytest.raises(DescricaoEmBrancoException):
#             deducao.setDeducao("")



