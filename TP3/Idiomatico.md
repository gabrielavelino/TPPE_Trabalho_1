# Idiomático

Por definição do dicionário Michaelis, a palavra "idiomático" significa "1. Relativo a idioma. 2. Característico ou próprio de determinado idioma.". 

Ou seja, "idiomático" é um termo que se refere ao uso correto e apropriado de uma linguagem específica, seja ela uma língua natural ou uma linguagem de programação. No caso de código, isso significa que ele segue as convenções, padrões e melhores práticas estabelecidos para aquela linguagem de programação em particular, tornando-o fácil de ser entendido por outros desenvolvedores que usam a mesma linguagem de programação e tornando o desenvolvimento mais eficiente. Além disso, o uso de código idiomático geralmente resulta em soluções mais elegantes, escaláveis e de fácil manutenção, já que isso torna mais fácil alterá-lo.

A prática de tornar um código idiomático é bastante utilzada principalmente na linguagem Python, que possui naturalmente uma grande quantidade de funções _built-in_ disponíveis ao desenvolvedor. Essa característica reforça o objetivo de justamente tornar o código mais legível e simples e pode ser observada aqui:

Exemplo de código não idiomático:
```python
names = []
for i in range(5):
    name = input("Insira o nome: ")
    names.append(name)

print("Nomes inseridos:")
for i in range(len(names)):
    print("Nome {}: {}".format(i+1, names[i]))
```

Exemplo de código idiomático:
```python
names = [input("Insira o nome: ") for _ in range(5)]

print("Nomes inseridos:")
for i, name in enumerate(names, start=1):
    print(f"Nome {i}: {name}")
```

Na versão idiomática, é utilizada uma compreensão de lista para coletar os nomes, em vez de um _loop for_ explícito e um _append_ para adicioná-los à lista. Além disso, na impressão dos nomes, é utilizada a função _enumerate_ para obter o índice do nome e imprimi-lo junto com o nome, em vez de calcular o índice manualmente e usar o método _format_. A função _enumerate_ também permite especificar o valor inicial do índice, evitando a necessidade de somar 1 manualmente a cada iteração.

Quando o código é mais idiomático, isso tem vários efeitos positivos na estrutura, claridade, coesão e acoplamento:

- **Estrutura**: O código idiomático segue as convenções e padrões estabelecidos pela comunidade, tornando-o mais fácil de ser entendido e mantido por outros programadores.

- **Claridade**: O código idiomático tende a ser mais claro e conciso, com nomes de variáveis e funções significativos e menos código desnecessário. Isso torna o código mais fácil de ser lido e compreendido.

- **Coesão**: O código idiomático tende a ser mais coeso, ou seja, as partes do código trabalham juntas de forma mais lógica e eficiente, sem código desnecessário ou redundante.

- **Acoplamento**: O código idiomático tende a ter menos acoplamento, ou seja, as partes do código são menos dependentes umas das outras. Isso torna o código mais fácil de ser alterado e mantido sem prejudicar outras partes do código.

Em resumo, tornar o código mais idiomático aumenta a sua facilidade de leitura, manutenção e ajuste. Além disso, ajuda a garantir a qualidade do código e a sua capacidade de evoluir com o tempo.

## Eliminando maus-cheiros de código

Um código ser idiomático ajuda a eliminar maus-cheiros de código citados por Martin Fowler, em seu livro "_Refactoring: Improving the Design of Existing Code_", como: código duplicado, método longo e classe inchada, lista de parâmetros longa demais, cirurgia com rifle, dentre outros. Sendo que, um código idiomático por natureza evita a criação de maus-cheiros, pois ele segue as boas práticas que a documentação e a comunidade lentamente foram construindo.

No exemplo de um código duplicado ser considerado um mau-cheiro de código, o uso de funções ou classes próprias da linguagem para encapsular essa lógica é uma forma idiomática de resolver esse problema. De maneira semelhante, o uso de expressões ternárias ou o aproveitamento das funcionalidades dos métodos padrão de uma classe, em vez de escrever código customizado, são formas idiomáticas de resolver outros tipos de maus-cheiros de código. Em resumo, o código idiomático é uma forma de ajudar a identificar e eliminar maus-cheiros de código, tornando o código mais limpo e fácil de manter.

## Exemplo de refatoração utilizando código idiomático

Um exemplo de operação de refatoração que pode ser aplicada para favorecer a idiomatização de um código é a decomposição de definições longas em iterações. Esta operação de refatoração é muito útil para favorecer a idiomatização de um código, pois ela permite que o código fique menor, favorecendo a eliminação de um método longo.

Exemplo de método longo e duplicação no nosso código:
```python
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
    print(f"Base de cálculo total: {base_total}  |   Valor total do imposto: {resultado_final['faixa_5']['valor_imposto']}\n")
```
Exemplo de refatoração de maneira idiomática, utilizando _f-strings_ do Python, evitando o mau-cheiro de método longo e duplicação:
```python
    for i in range(1, 6):
        print(f"{i}ª Faixa")
        faixa = resultado_final[f'faixa_{i}']
        print(f"Base de cálculo: {faixa['valor_base']}  |   Valor do imposto: {faixa['valor_imposto']}")

    print(f"Base total: {base_total}  |   Valor total do imposto: {imposto_total}")
```