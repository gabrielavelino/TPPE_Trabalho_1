from Rendimentos import Rendimento
from Deducoes import Deducoes
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

    while quantidadeDeducoes > 0:
        descriçao = str(input("Digite a descrição da sua dedução: "))
        deducao.setDeducao(descriçao)
        valor = float(input("Digite o valor da sua dedução: "))
        deducao.setValorDeducao(valor)
        print("A descrição da sua dedução é: ", deducao.getDeducao())
        print("O valor da sua dedução é: ", deducao.getValorDeducao())
        quantidadeDeducoes = quantidadeDeducoes - 1
        

if __name__ == "__main__":
    main()