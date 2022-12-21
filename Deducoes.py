
class Deducoes:
    def __init__(self,deducao =  '',valor = 0):
        self.deducao = deducao
        self.valorDeducao = valor
        pass
    
    def getValorDeducao(self):
        return self.valorDeducao
    def  setValorDeducao(self,valor):
        self.valorDeducao = valor
    def  getDeducao(self):
        return self.deducao
    def  setDeducao(self,deducao):
        self.deducao = deducao

    def CalculaDeducoes(self, valorDeducao):
        return valorDeducao + self.valorDeducao
        