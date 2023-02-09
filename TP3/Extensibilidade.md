# Extensibilidade

A extensibilidade é uma característica que representa a possibilidade de ser facilmente expandido no futuro. Um projeto é bom quando ele possui essa possibilidade. No final das contas, significa que devem ser flexíveis o suficiente para que a adição de novas funcionalidades, robustez e novos recursos não exijam uma reestruturação imensa do código.

É uma característica que "conversa" muito com as outras justamente porque a aplicação das outras características é o que vai dar ao projeto essa possibilidade de extensão.

Existem algumas formas de tornar um projeto com mais extensibilidade:

1. Modularizar o código: módulos bem definidos e independentes torna o desenvolvimento mais fácil, pois é mais raro elas afetarem diretamente o restante do código.

2. Evitar soluções ad-hoc: ao invés de aplicar soluções específicas, a busca aqui é tratar com soluções mais gerais e que sejam flexíveis.

3. Padrões de projeto: nada melhor do que ter um padrão bem definido, de forma com que todos os desenvolvedores saibam exatamente o que é esperado do código.

4. Documentação: explicações de como funciona o código é bem importante para que os desenvolvedores tenham total ciência do código e que a adição de novas pessoas na equipe tenham um adaptação mais rápida.


## Eliminando maus-cheiros de código

- A extensibilidade ajuda a reduzir os maus cheiros quando busca diminuir diversos possíveis problemas que podem aparecer no meio do caminho. 

Por exemplo, nesse sentido, evita-se a repetição do código já que é muito mais inteligente reescrever uma parte do código para que possa se adaptar a nova função do que criar uma nova parte que pouco difere da primeira. Além disso, ajuda também quando se prioriza soluções flexíveis a soluções rígidas e específicas, sem mencionar nos benefícios que os padrões do projeto e a modulizarização trazem ao código.

## Exemplo de refatoração utilizando código mais elegante

No caso abaixo, o cálculo da faixa 4 é meio obscuro. Não se sabe exatamente o que aqueles valores significam, e para um desenvolvedor que não tenha participado dessa parte do código, pode ficar bem complicado de se entender. Para um projeto que busca escala e extensibilidade, não é uma opção muito recomendada soluções desse tipo.  

Trecho de código antes da refatoração:

```python
if self.rendimentos > 3751.05 and self.rendimentos <= 4664.68:

    [...]

    calculo_faixas['faixa_4']['valor_imposto'] = round(((self.rendimentos / 100) * 15 - 354.8), 2)
    calculo_faixas['faixa_4']['valor_base'] = self.rendimentos - self.tabela['faixa_3']['max']

    return calculo_faixas
```

Segue abaixo uma solução bem mais inteligente do código de forma com que o código se faça mais entendível, otimizando tempo para o desenvolvedor, e consequentemente para o projeto como um todo.

```python
aliquota = 15
parcela_deducao = 354.8

if self.rendimentos > 3751.05:
    calculo_faixas['faixa_4']['valor_imposto'] = round(((self.rendimentos * aliquota / 100) - parcela_deducao), 2)
```
