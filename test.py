# -*- coding: utf-8 -*-

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
    ('filho','Filha','Teste','Boni',250,250,500,'30/08/2000',1189.55),
    ('Tia','Amiga','Previdencia','Avelox',250,250,400,'30/08/1990',1089.55)
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
def testCalculaRendimentoFalsicacao():
    rendimento = Rendimento('rendimento', 2)
    assert rendimento.CalculaRendimento() == 2

@pytest.mark.TesteFuncional
def testCalculaRendimentoDuplicacao():
    valor = 1500
    rendimento = Rendimento('rendimento', valor)
    assert rendimento.CalculaRendimento() == valor

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

@pytest.mark.parametrize("descricaoAli1,descricaoAli2,descricaoDedu,nome,valor1,valo2,valor3,dataNasci,valorTest", deducao)
def testCadastroTotalParametrizado(descricaoAli1,descricaoAli2,descricaoDedu,nome,valor1,valo2,valor3,dataNasci,valorTest):
    deducao = Deducoes()
    deducao.cadastrarPensaoAlimenticia(descricaoAli1,valor1)
    deducao.cadastrarPensaoAlimenticia(descricaoAli2,valo2)
    deducao.cadastrarDeducao(descricaoDedu,valor3)
    deducao.cadastrarDependentes(nome,dataNasci) # 1 dependente = 189,55
    
    assert deducao.CalculaDeducoes() == valorTest

    
# @pytest.mark.TesteExcecao
# def testDescricaoEmBrancoOutrasDeducoes():
#         deducao = Deducoes()
#         with pytest.raises(DescricaoEmBrancoException):
#             deducao.setDeducao("")



