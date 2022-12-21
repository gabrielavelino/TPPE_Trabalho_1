from Exceptions_test import ValorDeducaoInvalidoException, NomeEmBrancoException

class Deducoes:
    def __init__(self,deducao =  '',valor = 0):
        self.deducao = deducao
        self.valorDeducao = valor
        pass
    
    def getValorDeducao(self):
        return self.valorDeducao
    def  setValorDeducao(self,valor):
        if valor == 0:
            raise ValorDeducaoInvalidoException("Valor da dedução inválido! Digite um valor válido!")
        self.valorDeducao = valor
    def  getDeducao(self):
        return self.deducao
    def  setDeducao(self,deducao):
        if deducao == '':
            raise NomeEmBrancoException("Descrição da dedução em branco! Digite uma descrição válida!")
        self.deducao = deducao

    def CalculaDeducoes(self, valorDeducao):
        return valorDeducao + self.valorDeducao
        