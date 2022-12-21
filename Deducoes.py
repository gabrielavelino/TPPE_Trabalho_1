from Exceptions_test import ValorDeducaoInvalidoException, NomeEmBrancoException

class Deducoes:
    def __init__(self,deducao,valor):
        self.deducao = deducao
        self.valor = valor

    def getValorDeducao(self):
        return self.valor
    def  setValorDeducao(self,valor):
        if valor == 0:
            raise ValorDeducaoInvalidoException("Valor da dedução inválido! Digite um valor válido!")
        self.valor = valor
    
    def  getDeducao(self):
        return self.deducao
    def  setDeducao(self,deducao):
        if deducao == '':
            raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!")
        self.deducao = deducao

    def CalculaDeducoes(self,listDeducao):
        return sum(listDeducao)
        