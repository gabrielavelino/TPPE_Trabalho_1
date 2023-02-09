# Simplicidade

A simplicidade de código é uma característica que busca tornar o código fácil de ser compreendido, mantido e lido. Isso é alcançado por meio de técnicas como a escrita clara e concisa do código, a utilização de nomes de variáveis e funções descritivos, a organização do código em blocos distintos e a minimização do uso de recursos complexos ou pouco conhecidos. A simplicidade de código é importante porque garante a eficiência do desenvolvimento, facilita a manutenção do código e aprimora a capacidade de colaboração entre os membros da equipe de desenvolvimento.

A Simplicidade segue a filosofia de "Less is more", ou seja, é melhor desenvolver um código pequeno e abrangente do que algo complexo com poucas funcionalidades. Infelizmente, ainda há uma percepção equivocada de que a complexidade é algo positivo em projetos de desenvolvimento, mas na verdade ela esconde erros, dificulta a manutenção e complica a leitura do código, mesmo dentro da equipe ou organização. Por isso, é importante que programadores busquem sempre a simplicidade e desenvolvam o código o mais simples possível, aperfeiçoando suas habilidades.



## Eliminando maus-cheiros de código

A simplificação de um código ajuda na eliminação de maus-cheiros, visto que um código simples é mais fácil de entender e de poder realizar uma eventual manutenção. Alguns exemplos de mal-cheiros definidos por Fowler que podem ser eliminados: nome de variáveis bem definidos, códigos duplicados, métodos e classes grandes que realizam mais de uma função. Ou seja, a simplicidade possui um grande potencial na refatoração de códigos e na eliminação de maus-cheiros.


## Exemplo de refatoraçao utilizando Simplicidade

Um exemplo de operação de refatoração que pode ser aplicada para favorecer a simplicidade de um código é reduzir seu tamanho original, descartando linhas desnecessárias. Favorecendo a simplicidade do código, pois ela permite que o código fique mais legível e mais fácil de ser entendido, além de da facilidade em trabalhar com suporte. No exemplo abaixo, foi utilizado o método de refatoração de redução de tamanho de código, que consiste em remover linhas de código que não são necessárias para o funcionamento do programa. Um exemplo foi um dos códigos refatorados no TP2, 

- Exemplo de código original em Python:
```python
def valor_imposto(self,aliquota,deducao):
    rendimentosDiv = self.rendimentos / 100
    resultado = aliquota - deducao
    return round(((self.rendimentos / 100) * resultado), 2)
```

- Exemplo de código refatorado em Python:
```python
def valor_imposto(self, aliquota, deducao):
        return round(((self._rendimentos / 100) * aliquota - deducao), 2)

```