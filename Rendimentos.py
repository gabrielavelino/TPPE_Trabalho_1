
class Rendimento:
    
    def __init__(self,descricao =  '',valor = 0):
        self.descricao = descricao
        self.valor = valor
        pass

    def getValor(self):
        return self.valor
    def setValor(self,valor):
        self.valor = valor
    def getDescricao(self):
        return self.descricao
    def setDescricao(self,descricao):
        self.descricao = descricao
    

    def CalculaRendimento(self):
        return self.valor == 1