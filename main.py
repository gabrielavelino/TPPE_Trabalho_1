# -*- coding: utf-8 -*-

from Rendimentos import Rendimento
from Deducoes import Deducoes
from Faixa import Faixa
from Aliquota import Aliquota
rendimento = Rendimento()
deducao = Deducoes()

def main():

    print("============= Calculadora IRPF =============")
    descriçao = str(input("Digite a descrição do seu rendimento: "))
    rendimento.setDescricao(descriçao)
    valor = float(input("Digite o valor do seu rendimento: "))
    rendimento.setValor(valor)
    
    print("A descrição do seu rendimento é: ", rendimento.getDescricao())
    print("O valor do seu rendimento é: ", rendimento.getValor())

    quantidadeDeducoes = int(input("Digite a quantidade de deduções que você possui: "))
    #listDeducao = []
    
    while quantidadeDeducoes > 0:

        descriçao = str(input("Digite a descrição da sua dedução: "))
        #deducao.setDeducao(descriçao)

        valor = float(input("Digite o valor da sua dedução: "))

        deducao.cadastrarDeducao(descriçao, valor)

        #deducao.setValorDeducao(valor)

        #print("A descrição da sua dedução é: ", deducao.getDeducao())
        #print("O valor da sua dedução é: ", deducao.getValorDeducao())

        #listDeducao.append(deducao.getValorDeducao())
        quantidadeDeducoes = quantidadeDeducoes - 1

    #print('Valor total deducao: ', deducao.CalculaDeducoes())
    #print('Valor total deducao: ', deducao.CalculaDeducoes(listDeducao))

    #total = rendimento.getValor() - deducao.CalculaDeducoes(listDeducao)

    #print('Valor total rendimento: ',total)

    quantidadePrevidenciaria = int(input("Digite a quantidade de previdência oficial que você possui: "))

    while quantidadePrevidenciaria > 0:

        descriçaoPrevidenciaria = str(input("Digite a descrição da sua previdenciária oficial: "))
        valorPrevidenciaria = float(input("Digite o valor da sua previdencia oficial: "))

        deducao.cadastrarPrevidenciaOficial(descriçaoPrevidenciaria, valorPrevidenciaria)

        quantidadePrevidenciaria = quantidadePrevidenciaria - 1









    
    quantidadePensao = int(input("Digite a quantidade de pensões alimentícias que você possui: "))

    while quantidadePensao > 0:

        descriçaoPensao = str(input("Digite a descrição da sua pensão alimentícia: "))
        valorPensao = float(input("Digite o valor da sua pensão alimentícia: "))

        deducao.cadastrarPensaoAlimenticia(descriçaoPensao, valorPensao)

        quantidadePensao = quantidadePensao - 1





    
    quantidadeDependentes = int(input("Digite a quantidade de dependentes que você possui: "))

    while quantidadeDependentes > 0:

        descriçaoDependentes = str(input("Digite o nome do dependente: "))
        dataNascDependentes = str(input("Digite a data de nascimento: "))
        
        deducao.cadastrarDependentes(descriçaoDependentes, dataNascDependentes)
        #valorDependentes = float(input("Digite o valor da sua pensões alimentícias: "))
        quantidadeDependentes = quantidadeDependentes - 1

    
    
    valor_rendimento = rendimento.getValor()
    print('Rendimento: ', valor_rendimento)

    valor_deducao =  deducao.CalculaDeducoes()
    print('Valor total deducao: ', valor_deducao)

    total = valor_rendimento - valor_deducao
    print('Valor base: ',total)
        

    faixa = Faixa(total)

    resultado_final = faixa.calcular_imposto()

    base_total = resultado_final['faixa_1']['valor_base'] + resultado_final['faixa_2']['valor_base'] + resultado_final['faixa_3']['valor_base'] + resultado_final['faixa_4']['valor_base'] + resultado_final['faixa_5']['valor_base']
    imposto_total = resultado_final['faixa_5']['valor_imposto'] + resultado_final['faixa_4']['valor_imposto'] + resultado_final['faixa_3']['valor_imposto'] + resultado_final['faixa_2']['valor_imposto'] + resultado_final['faixa_1']['valor_imposto']

    print("1ª Faixa")
    print(f"Base de cálculo: {resultado_final['faixa_1']['valor_base']}  |   Valor do imposto: {resultado_final['faixa_1']['valor_imposto']}")
    print("2ª Faixa")
    print(f"Base de cálculo: {resultado_final['faixa_2']['valor_base']}  |   Valor do imposto: {resultado_final['faixa_2']['valor_imposto']}")
    print("3ª Faixa")
    print(f"Base de cálculo: {resultado_final['faixa_3']['valor_base']}  |   Valor do imposto: {resultado_final['faixa_3']['valor_imposto']}")
    print("4ª Faixa")
    print(f"Base de cálculo: {resultado_final['faixa_4']['valor_base']}  |   Valor do imposto: {resultado_final['faixa_4']['valor_imposto']}")
    print("5ª Faixa")
    print(f"Base de cálculo: {resultado_final['faixa_5']['valor_base']}  |   Valor do imposto: {resultado_final['faixa_5']['valor_imposto']}\n")
    print(f"Base de cálculo total: {base_total}  |   Valor total do imposto: {imposto_total}\n")

    aliquota = Aliquota(imposto_total, base_total)
    valor_final_aliquota = aliquota.calcular_aliquota()

    print(f"Alíquota efetiva: {valor_final_aliquota}%")




if __name__ == "__main__":
    main()