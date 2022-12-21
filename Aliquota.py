class Aliquota:

    def __init__(self, valor_base, imposto):
        self.valor_base = valor_base
        self.imposto = imposto

    def calcular_aliquota(self):
        return 2