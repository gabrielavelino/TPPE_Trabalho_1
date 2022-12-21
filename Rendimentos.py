
class Rendimento:
    
    def __init__(self,descricao,valor):
        self.descricao = descricao
        self.valor = valor
        pass

    def CalculaRendimento(self):
        return self.valor == 1