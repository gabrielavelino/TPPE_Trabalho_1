# Modularidade (baixo acoplamento e alta coesão)

A modularidade é a habilidade de dividir um sistema em partes autônomas, que podem ser criadas e testadas individualmente. Essas partes são conhecidas como módulos, funções ou procedimentos. É um dos princípios mais cruciais da engenharia de software, uma vez que possibilita o desenvolvimento mais rápido e eficiente do sistema. Além disso, a modularidade torna o sistema mais fácil de manter, desacoplar um módulo e evoluir o programa.

Existem qualidades chaves da modularização que caracterizam um bom módulo, são elas:

  * Baixo acoplamento
  * Alta coesão

## Baixo acoplamento

Acoplamento é a medida da interdependência entre módulos. Módulos com baixo acoplamento dependem de poucos outros, enquanto módulos com alto acoplamento dependem de muitos. Módulos com alto acoplamento são conhecidos como "módulos espaguete" e são mais difíceis de serem mantidos e evoluídos. Já módulos com baixo acoplamento são mais fáceis de serem gerenciados e aperfeiçoados. Ao desenvolver um módulo com alto acoplamento, pode ser necessário modificar muitos outros, tornando a manutenção e evolução mais desafiadoras. Por isso, o baixo acoplamento é um dos princípios mais importantes da engenharia de software, garantindo eficiência no desenvolvimento e qualidade no software.

## Alta coesão

Coesão é a medida da relação entre as responsabilidades de um módulo. Um módulo com alta coesão é aquele que tem uma única responsabilidade. Um módulo com baixa coesão é aquele que tem várias responsabilidades. Um módulo com baixa coesão é mais difícil de ser mantido e evoluído, pois ele tem várias responsabilidades. Um módulo com alta coesão é mais fácil de ser mantido e evoluído, pois ele tem uma única responsabilidade. Módulos com baixa coesão, dificulta na hora de modificar, pois terá que mexer em outros trechos de código para mudar apenas uma funcionalidade, que não aconteceria se a modularização estivesse correta, onde mexeria em um trecho específico de código para melhorâ-lo, retirar ou fazer manutenções.

## Relação de modularização com maus cheiros de código

A modularização é importante para eliminar vários tipos de maus-cheiros bem como evitar pela raiz, que isso aconteça futuramente. Alguns dos maus-cheiros que podem ser evitados: 

- <b>Método longo</b>: Métodos longos refutam a alta coesão de um módulo, pois automaticamente são feitos para resolver mais de uma responsabilidade. Isto faz com que as mudanças e modificações sejam feitas e assim alterem consequentemente grande parte do código, oiu seja, um método longo também refuta o baixo acoplamento de um módulo. 

- <b>Lista de parâmetros longa demais</b>: Aqui podemos ver que a modularização também é uma forma de evitar o mau cheiro de lista de parâmetros longa demais, pois ao modularizar o código, o programador pode criar funções e procedimentos que recebam parâmetros e retornem valores, assim evitando que o programador tenha que passar muitos parâmetros para uma função ou procedimento. Aqui podemos recomendar o envio de objetos como parâmetros, pois assim o programador pode enviar apenas um objeto para a função ou procedimento, e assim evitar a lista de parâmetros longa demais.

- <b>Cirurgia com rifle </b>: É importante garantir que as mudanças sejam feitas no próprio módulo, mantendo o mesmo retorno, ou tratar o retorno corretamente para evitar mudanças em vários pontos diferentes.


- <b>Homem do meio </b>: Existem funções que são chamadas para no fim chamarem outras funções, isto faz com que existam condições que encaminham para outras funções e assim por diante, o que pode dificultar a manutenção do código. É importante evitar a criação de funções que chamem outras funções, pois isso pode dificultar a manutenção do código.

## Exemplo de refatoração utilizando modularização

Um exemplo para refatorar usando modularização no arquivo main.py, é possível separar esse bloco de print para que seja uma função que retorne apenas isso:

```python
# Linha 113
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
# Linha 130
```

Com a refatoração é adicionado uma função para a leitura desses parâmetros, separando-a da função main, para um eventual ajuste na formatação da tabela.

```python

def imprime_tabela(resultado_final,base_total):
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

def main:
    imprime_tabela(resultado,baseTotal)

```