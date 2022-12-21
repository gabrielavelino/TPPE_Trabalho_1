from Rendimentos import Rendimento

rendimento = Rendimento()

def main():
    print("============= Calculadora IRPF =============")
    valor = float(input("Digite o valor do seu rendimento: "))
    rendimento.setValor(valor)
    descriçao = str(input("Digite a descrição do seu rendimento: "))
    rendimento.setDescricao(descriçao)
    print("O valor do seu rendimento é: ", rendimento.getValor())
    print("A descrição do seu rendimento é: ", rendimento.getDescricao())


if __name__ == "__main__":
    main()