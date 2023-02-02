import math
from tabela import tabela_faixa


class Faixa:

    def __init__(self, rendimentos):
        self.rendimentos = rendimentos
        self.calculadora = CalculadoraImposto(self.rendimentos)

    def gerar_faixa(self):
        faixa = self.calculadora.computar()
        return faixa


class CalculadoraImposto:

    def __init__(self, rendimentos):
        self._rendimentos = rendimentos
        self._tabela = tabela_faixa
        self._calculo_faixas = {
            'faixa_1': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
            'total': { 'valor_imposto': 0, 'valor_base': 0 }
        }

    def valor_imposto(self,aliquota, deducao):
        return round(((self._rendimentos / 100) * aliquota - deducao), 2)

    def valor_base(self, faixa):
        return self._rendimentos - self._tabela[faixa]['max']

    def incide_sobre_faixa_1(self):
        return self._calculo_faixas

    def incide_sobre_faixa_2(self):

        self._calculo_faixas['faixa_1']['valor_imposto'] = 0
        self._calculo_faixas['faixa_1']['valor_base'] = 1903.98
        self._calculo_faixas['faixa_2']['valor_imposto'] = self.valor_imposto(7.5, 142.8)
        self._calculo_faixas['faixa_2']['valor_base'] = self.valor_base('faixa_1')

        return self.calculo_faixas

    def incide_sobre_faixa_3(self):

        self._calculo_faixas['faixa_1']['valor_imposto'] = 0
        self._calculo_faixas['faixa_1']['valor_base'] = 1903.98
        self._calculo_faixas['faixa_2']['valor_imposto'] = 69.20
        self._calculo_faixas['faixa_2']['valor_base'] = 922.67
        self._calculo_faixas['faixa_3']['valor_imposto'] = self.valor_imposto(15, 354.8)
        self._calculo_faixas['faixa_3']['valor_base'] = self.valor_base('faixa_2')

        return self._calculo_faixas

    def incide_sobre_faixa_4(self):

        self._calculo_faixas['faixa_1']['valor_imposto'] = 0
        self._calculo_faixas['faixa_1']['valor_base'] = 1903.98
        self._calculo_faixas['faixa_2']['valor_imposto'] = 69.20
        self._calculo_faixas['faixa_2']['valor_base'] = 922.67
        self._calculo_faixas['faixa_3']['valor_imposto'] = 138.66
        self._calculo_faixas['faixa_3']['valor_base'] = 924.40
        self._calculo_faixas['faixa_4']['valor_imposto'] = self.valor_imposto(22.5, 636.13)
        self._calculo_faixas['faixa_4']['valor_base'] = self.valor_base('faixa_3')

        return self._calculo_faixas

    def incide_sobre_faixa_5(self):

        self._calculo_faixas['faixa_1']['valor_imposto'] = 0
        self._calculo_faixas['faixa_1']['valor_base'] = 1903.98
        self._calculo_faixas['faixa_2']['valor_imposto'] = 69.20
        self._calculo_faixas['faixa_2']['valor_base'] = 922.67
        self._calculo_faixas['faixa_3']['valor_imposto'] = 138.66
        self._calculo_faixas['faixa_3']['valor_base'] = 924.40
        self._calculo_faixas['faixa_4']['valor_imposto'] = 205.56
        self._calculo_faixas['faixa_4']['valor_base'] = 913.63
        self._calculo_faixas['faixa_5']['valor_imposto'] = self.valor_imposto(27.5, 869.36)
        self._calculo_faixas['faixa_5']['valor_base'] = self.valor_base('faixa_4')

        return self._calculo_faixas

    def computar(self):

        if self._rendimentos <= 1903.98:
            return self.incide_sobre_faixa_1()

        elif self._rendimentos > 1903.98 and self._rendimentos <= 2826.65:
            return self.incide_sobre_faixa_2()

        elif self._rendimentos > 2826.65 and self._rendimentos <= 3751.05:
            return self.incide_sobre_faixa_3()
    
        elif self._rendimentos > 3751.05 and self._rendimentos <= 4664.68:
            return self.incide_sobre_faixa_4()

        elif self._rendimentos > 4664.68:
            return self.incide_sobre_faixa_5()