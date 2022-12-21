from Exceptions_test import ValorRendimentoInvalidoException, DescricaoEmBrancoException
class Rendimento:
    
    def __init__(self,descricao =  '',valor = 0):
        self.descricao = descricao
        self.valor = valor
        pass

    def getValor(self):
        return self.valor
    def setValor(self,valor):
        if valor == 0:
            raise ValorRendimentoInvalidoException("Valor do rendimento inválido! Digite um valor válido!")
        self.valor = valor
    def getDescricao(self):
        return self.descricao
    def setDescricao(self,descricao):
        if descricao == '':
            raise DescricaoEmBrancoException("Descrição do rendimento em branco! Digite uma descrição válida!")
        self.descricao = descricao
    

    def CalculaRendimento(self):
        return self.valor == 1