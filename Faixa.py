import math
from tabela import tabela_faixa

class Faixa:

    def __init__(self, rendimentos):
        self.rendimentos = rendimentos
        self.tabela = tabela_faixa

    def valor_imposto(self, aliquota, deducao):
        return round(((self.rendimentos / 100) * aliquota - deducao), 2)

    def valor_base(self, faixa):
        return self.rendimentos - self.tabela[faixa]['max']

    def calcular_imposto(self):

        calculo_faixas = {
            'faixa_1': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
            'total': { 'valor_imposto': 0, 'valor_base': 0 }
        }

        if self.rendimentos <= 1903.98:

            return calculo_faixas

        if self.rendimentos > 1903.98 and self.rendimentos <= 2826.65:

            calculo_faixas['faixa_1']['valor_imposto'] = 0
            calculo_faixas['faixa_1']['valor_base'] = 1903.98

            calculo_faixas['faixa_2']['valor_imposto'] = self.valor_imposto(7.5,142.8)
            calculo_faixas['faixa_2']['valor_base'] = self.valor_base('faixa_1')

            return calculo_faixas

        if self.rendimentos > 2826.65 and self.rendimentos <= 3751.05:

            calculo_faixas['faixa_1']['valor_imposto'] = 0
            calculo_faixas['faixa_1']['valor_base'] = 1903.98

            calculo_faixas['faixa_2']['valor_imposto'] = 69.20
            calculo_faixas['faixa_2']['valor_base'] = 922.67

            calculo_faixas['faixa_3']['valor_imposto'] = self.valor_imposto(15,354.8)
            calculo_faixas['faixa_3']['valor_base'] = self.valor_base('faixa_2')

            return calculo_faixas

        if self.rendimentos > 3751.05 and self.rendimentos <= 4664.68:

            calculo_faixas['faixa_1']['valor_imposto'] = 0
            calculo_faixas['faixa_1']['valor_base'] = 1903.98

            calculo_faixas['faixa_2']['valor_imposto'] = 69.20
            calculo_faixas['faixa_2']['valor_base'] = 922.67

            calculo_faixas['faixa_3']['valor_imposto'] = 138.66
            calculo_faixas['faixa_3']['valor_base'] = 924.40

            calculo_faixas['faixa_4']['valor_imposto'] = self.valor_imposto(22.5,636.13)
            calculo_faixas['faixa_4']['valor_base'] = self.valor_base('faixa_3')

            return calculo_faixas

        if self.rendimentos > 4664.68:

            calculo_faixas['faixa_1']['valor_imposto'] = 0
            calculo_faixas['faixa_1']['valor_base'] = 1903.98

            calculo_faixas['faixa_2']['valor_imposto'] = 69.20
            calculo_faixas['faixa_2']['valor_base'] = 922.67

            calculo_faixas['faixa_3']['valor_imposto'] = 138.66
            calculo_faixas['faixa_3']['valor_base'] = 924.40

            calculo_faixas['faixa_4']['valor_imposto'] = 205.56
            calculo_faixas['faixa_4']['valor_base'] = 913.63

            calculo_faixas['faixa_5']['valor_imposto'] = self.valor_imposto(27.5,869.36)
            calculo_faixas['faixa_5']['valor_base'] = self.valor_base('faixa_4')

            return calculo_faixas