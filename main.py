from Rendimentos import Rendimento
from Deducoes import Deducoes
rendimento = Rendimento()
deducao = Deducoes('',0)

def main():
    print("============= Calculadora IRPF =============")
    descriçao = str(input("Digite a descrição do seu rendimento: "))
    rendimento.setDescricao(descriçao)
    valor = float(input("Digite o valor do seu rendimento: "))
    rendimento.setValor(valor)
    
    print("A descrição do seu rendimento é: ", rendimento.getDescricao())
    print("O valor do seu rendimento é: ", rendimento.getValor())

    quantidadeDeducoes = int(input("Digite a quantidade de deduções que você possui: "))
    listDeducao = []
    while quantidadeDeducoes > 0:
        descriçao = str(input("Digite a descrição da sua dedução: "))
        deducao.setDeducao(descriçao)
        valor = float(input("Digite o valor da sua dedução: "))
        deducao.setValorDeducao(valor)
        print("A descrição da sua dedução é: ", deducao.getDeducao())
        print("O valor da sua dedução é: ", deducao.getValorDeducao())
        listDeducao.append(deducao.getValorDeducao())
        quantidadeDeducoes = quantidadeDeducoes - 1
    print('Valor total deducao: ', deducao.CalculaDeducoes(listDeducao))
    total = rendimento.getValor() - deducao.CalculaDeducoes(listDeducao)
    print('Valor total rendimento: ',total) 
        

if __name__ == "__main__":
    main()