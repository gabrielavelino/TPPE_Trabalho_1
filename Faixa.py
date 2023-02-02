tabela_fixos_por_faixa = {
    'faixa_1':{
        'piso': 0,
        'teto': 1903.98,
        'aliquota': 0,
        'deducao': 0,
        'base_maxima_se_ultrapassado': 1903.98,
        'imposto_se_ultrapassado': 0
    },
    'faixa_2':{
        'piso': 1903.99,
        'teto':2826.65,
        'aliquota': 7.5,
        'deducao': 142.8,
        'base_maxima_se_ultrapassado': 922.67,
        'imposto_se_ultrapassado': 69.20
    },
    'faixa_3':{
        'piso': 2826.66,
        'teto': 3751.05,
        'aliquota': 15,
        'deducao': 354.8,
        'base_maxima_se_ultrapassado': 924.40,
        'imposto_se_ultrapassado': 138.66
    },
    'faixa_4':{
        'piso': 3751.06,
        'teto':4664.68,
        'aliquota': 22.5,
        'deducao': 636.13,
        'base_maxima_se_ultrapassado': 913.63,
        'imposto_se_ultrapassado': 205.56
    },
    'faixa_5':{
        'piso': 4664.69,
        'teto': float('inf'),
        'aliquota': 27.5,
        'deducao': 869.36,
        'base_maxima_se_ultrapassado': 1903.98,
        'imposto_se_ultrapassado': 1903.98
    }
}

class Faixa:

    def __init__(self, rendimentos):
        self.rendimentos = rendimentos
        self.calculadora = CalculadoraImposto(self.rendimentos)

    def gerar_faixa(self):
        faixa = self.calculadora.calcular()
        return faixa


class CalculadoraImposto:

    def __init__(self, rendimentos):
        self._rendimentos = rendimentos
        self._tabela_fixos = tabela_fixos_por_faixa
        self._tabela_apuracao_imposto = {
            'faixa_1': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_2': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_3': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_4': { 'valor_imposto': 0, 'valor_base': 0 },
            'faixa_5': { 'valor_imposto': 0, 'valor_base': 0 },
            'total': { 'valor_imposto': 0, 'valor_base': 0 }
        }

    def valor_imposto(self, aliquota, deducao):
        return round(((self._rendimentos / 100) * aliquota - deducao), 2)

    def valor_base(self, faixa):
        return self._rendimentos - self._tabela_fixos[faixa]['teto']

    def incide_sobre_faixa_1(self):
        return self._tabela_apuracao_imposto

    def incide_sobre_faixa_2(self):

        self._tabela_apuracao_imposto['faixa_1']['valor_imposto'] = self._tabela_fixos['faixa_1']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_1']['valor_base'] = self._tabela_fixos['faixa_1']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_imposto'] = self.valor_imposto(self._tabela_fixos['faixa_2']['aliquota'], self._tabela_fixos['faixa_2']['deducao'])
        self._tabela_apuracao_imposto['faixa_2']['valor_base'] = self.valor_base('faixa_1')


        return self._tabela_apuracao_imposto

    def incide_sobre_faixa_3(self):

        self._tabela_apuracao_imposto['faixa_1']['valor_imposto'] = self._tabela_fixos['faixa_1']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_1']['valor_base'] = self._tabela_fixos['faixa_1']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_imposto'] = self._tabela_fixos['faixa_2']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_base'] = self._tabela_fixos['faixa_2']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_3']['valor_imposto'] = self.valor_imposto(self._tabela_fixos['faixa_3']['aliquota'], self._tabela_fixos['faixa_3']['deducao'])
        self._tabela_apuracao_imposto['faixa_3']['valor_base'] = self.valor_base('faixa_2')

        return self._tabela_apuracao_imposto

    def incide_sobre_faixa_4(self):

        self._tabela_apuracao_imposto['faixa_1']['valor_imposto'] = self._tabela_fixos['faixa_1']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_1']['valor_base'] = self._tabela_fixos['faixa_1']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_imposto'] = self._tabela_fixos['faixa_2']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_base'] = self._tabela_fixos['faixa_2']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_3']['valor_imposto'] = self._tabela_fixos['faixa_3']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_3']['valor_base'] = self._tabela_fixos['faixa_3']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_4']['valor_imposto'] = self.valor_imposto(self._tabela_fixos['faixa_4']['aliquota'], self._tabela_fixos['faixa_4']['deducao'])
        self._tabela_apuracao_imposto['faixa_4']['valor_base'] = self.valor_base('faixa_3')

        return self._tabela_apuracao_imposto

    def incide_sobre_faixa_5(self):

        self._tabela_apuracao_imposto['faixa_1']['valor_imposto'] = self._tabela_fixos['faixa_1']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_1']['valor_base'] = self._tabela_fixos['faixa_1']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_imposto'] = self._tabela_fixos['faixa_2']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_2']['valor_base'] = self._tabela_fixos['faixa_2']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_3']['valor_imposto'] = self._tabela_fixos['faixa_3']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_3']['valor_base'] = self._tabela_fixos['faixa_3']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_4']['valor_imposto'] = self._tabela_fixos['faixa_4']['imposto_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_4']['valor_base'] = self._tabela_fixos['faixa_4']['base_maxima_se_ultrapassado']
        self._tabela_apuracao_imposto['faixa_5']['valor_imposto'] = self.valor_imposto(self._tabela_fixos['faixa_5']['aliquota'], self._tabela_fixos['faixa_5']['deducao'])
        self._tabela_apuracao_imposto['faixa_5']['valor_base'] = self.valor_base('faixa_4')

        return self._tabela_apuracao_imposto

    def calcular(self):

        if self._rendimentos <= self._tabela_fixos['faixa_1']['teto']:
            return self.incide_sobre_faixa_1()

        elif self._rendimentos > self._tabela_fixos['faixa_2']['piso'] and self._rendimentos <= self._tabela_fixos['faixa_2']['teto']:
            return self.incide_sobre_faixa_2()

        elif self._rendimentos > self._tabela_fixos['faixa_3']['piso'] and self._rendimentos <= self._tabela_fixos['faixa_3']['teto']:
            return self.incide_sobre_faixa_3()
    
        elif self._rendimentos > self._tabela_fixos['faixa_4']['piso'] and self._rendimentos <= self._tabela_fixos['faixa_4']['teto']:
            return self.incide_sobre_faixa_4()

        elif self._rendimentos > self._tabela_fixos['faixa_5']['piso']:
            return self.incide_sobre_faixa_5()