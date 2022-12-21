# -*- coding: utf-8 -*-

from Exceptions_test import ValorDeducaoInvalidoException, NomeEmBrancoException

class Deducoes:
    def __init__(self):
        self.deducoes = []
        self.previdenciaOficial = []
        self.pensaoAlimenticia = []
        self.dependentes = []
        self.totalValorDeducao = 0.0
    
    def cadastrarDeducao(self,deducao,valorDeducao):
        if deducao == '' or None:
            raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!")
        elif valorDeducao == 0 or None:
            raise ValorDeducaoInvalidoException("Valor da dedução inválido! Digite um valor válido!")
        
        deducaoDict = {"descricao": deducao, "valor": valorDeducao}
        self.deducoes.append(deducaoDict)
        self.totalValorDeducao += valorDeducao
    
    def cadastrarPrevidenciaOficial(self,descPrevidencia,valorPrevidencia):
        if descPrevidencia == '' or None:
            raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!")
        elif valorPrevidencia == 0 or None:
            raise ValorDeducaoInvalidoException("Valor da dedução inválido! Digite um valor válido!")

        PrevidenciaDict = {"descricao": descPrevidencia, "valor": valorPrevidencia}

        self.previdenciaOficial.append(PrevidenciaDict)
        self.totalValorDeducao += valorPrevidencia

    def cadastrarPensaoAlimenticia(self,descPensao,valorPensao):
        if descPensao == '' or None:
            raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!")
        elif valorPensao == 0 or None:
            raise ValorDeducaoInvalidoException("Valor da dedução inválido! Digite um valor válido!")

        PensaoDict = {"descricao": descPensao, "valor": valorPensao}

        self.pensaoAlimenticia.append(PensaoDict)
        self.totalValorDeducao += valorPensao
    
    def cadastrarDependentes(self,nome,dataNascimento):
        if nome == '' or None:
            raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!") 

        DependenteDict = {"Nome": nome, "DataNascimento": dataNascimento}

        self.dependentes.append(DependenteDict)
    
    def getDeducoes(self):
        return self.deducoes
    
    def getPrevidenciaOficial(self):
        return self.previdenciaOficial
    
    def getPensaoAlimenticia(self):
        return self.pensaoAlimenticia
    
    def getDependentes(self):
        return self.dependentes
    
    def getDependentes(self):
        NumDependentes = len(self.dependentes)
        return NumDependentes

    def CalculaDeducoes(self):
        self.totalValorDeducao  = self.totalValorDeducao +(189.55 * len(self.dependentes))
        return self.totalValorDeducao 

    # def getValorDeducao(self):
    #     return self.valorDeducao
    # def  setValorDeducao(self,valor):
    #     if valor == 0:
    #         raise ValorDeducaoInvalidoException("Valor da dedução inválido! Digite um valor válido!")
    #     self.valorDeducao = valor
    # def  getDeducao(self):
    #     return self.deducao
    # def  setDeducao(self,deducao):
    #     if deducao == '':
    #         raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!")
    #     self.deducao = deducao

    # def CalculaDeducoes(self,listDeducao):
    #     return sum(listDeducao)
        