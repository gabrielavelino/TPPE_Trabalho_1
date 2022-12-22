class Aliquota:

    def __init__(self, imposto, valor_base):
        self.imposto = imposto
        self.valor_base = valor_base

    def calcular_aliquota(self):
        aliquota = (self.imposto / self.valor_base) * 100
        return round(aliquota,2)