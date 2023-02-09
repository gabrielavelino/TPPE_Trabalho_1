# Elegância

Um código elegante é aquele que é escrito de maneira clara, concisa, legível, e eficiente. É um código que usa as melhores práticas e convenções da linguagem, e que segue padrões comuns para resolver problemas de maneira eficaz.

Além disso, um código elegante deve ser fácil de manter e ajustar, mesmo se você ou outra pessoa não tiver escrito o código original. É importante notar que a elegância não se trata apenas de como o código se parece, mas também de como ele é projetado para funcionar e se integrar com outras partes do sistema.

A elegância de um código tem relação com a **estética** do projeto no sentido de diretamente relacionada com a simplicidade do código, ou seja, não se tem no código trechos muito complexos ou muito complicados de se entender ao revisá-lo. Um bom projeto possui estruturas agradáveis de se observar, e a beleza em sua estrutura pode ser observada quando o controle de cada trecho do código com seus elementos flui de maneira graciosa por todo o sistema.

Algumas características que compõem um código elegante são listadas no livro "_Code Craft : The Practice of Writing Excellent Code_", de Pete Goodliffe:

- Fluídez sensata ao longo do sistema, ou seja, operações que passam apenas pelos módulos necessários;
- Complemento e conexão entre as partes;
- Não há muitas exceções para as regras estabelecidas;
- Não existência de artimanhas (gambiarra) para solucionar os problemas;
- Mudanças em pequenos trechos do código não afetam muitos outros lugares.

Trazendo esses conceitos à prática, uma ideologia estética que é bastante praticada e citada pela comunidade de desenvolvedores é a estética _**pythônica**_. 

Aqui está um exemplo de transformação de código para ser mais elegante em Python:

Código não elegante:

```python
numbers = [1, 2, 3, 4, 5]
new_list = []
for num in numbers:
    if num % 2 == 0:
        new_list.append(num**2)
print(new_list)
```

Código elegante, ou um pouco mais _pythônico_:

```python
numbers = [1, 2, 3, 4, 5]
new_list = [num**2 for num in numbers if num % 2 == 0]
print(new_list)
```

Nesse exemplo, o código elegante usa a chamada _list comprehension_ para condensar as operações de filtragem e transformação em uma única linha de código, tornando-o mais conciso e legível. Além disso, _list comprehensions_ são uma característica comum da programação funcional em Python, por isso também se encaixam bem na estética _pythônica_.

## Eliminando maus-cheiros de código

Um código elegante e limpo tem uma relação direta com a eliminação de maus-cheiros de código, pois um código elegante tem as seguintes características:

- É fácil de entender e manter;
- Tem uma boa estrutura, coesão e acoplamento;
- É claro e conciso, evitando código duplicado ou redundante;
- Segue as convenções e boas práticas da linguagem;
- É otimizado para melhor desempenho.

Todas essas características são importantes para evitar maus-cheiros de código, como o código duplicado, o código complexo, o código com baixa coesão, entre outros. Portanto, ao tornar o código mais elegante, é possível melhorar a qualidade do código e evitar problemas futuros.

## Exemplo de refatoração utilizando código mais elegante

Um exemplo de refatoração que torne o código mais elegante é o _Rendimentos.py_, adicionando a ele elementos próprios da linguagem Python que torna o trabalho com a classe Rendimento mais otimizado, seguindo convenções da linguagem. Além de trazer uma estética visualmente mais agradável que o anterior, ele traz também algumas características que foram citadas anteriormente. A padronização diante das convenções evita que principalmente durante a manutenção o desenvolvedor possa vir a ter surpresas, por o design estar padronizado - fato que melhora tanto a visualização do desenvolvedor, quanto do próprio interpretador do Python.  

Código antes da refatoração:

```python
from Exceptions_test import ValorRendimentoInvalidoException, DescricaoEmBrancoException
class Rendimento:
    
    def __init__(self,descricao =  '',valor = 0):
        self.descricao = descricao
        self.valor = valor
        pass

    def getValor(self):
        return self.valor
    def setValor(self,valor):
        if valor == 0 or valor == None or valor < 0:
            raise ValorRendimentoInvalidoException("Valor do rendimento inválido! Digite um valor válido!")
        self.valor = valor
    
    def getDescricao(self):
        return self.descricao

    def setDescricao(self,descricao):
        if descricao == '' or descricao == None:
            raise DescricaoEmBrancoException("Descrição do rendimento em branco! Digite uma descrição válida!")
        self.descricao = descricao
    
    def CalculaRendimento(self):
        return self.valor
```

Código após refatoração que traz maior elegância, ou um pouco mais _pythônico_:

```python
from Exceptions_test import ValorRendimentoInvalidoException, DescricaoEmBrancoException

class Rendimento:
    def __init__(self, descricao: str = '', valor: float = 0.0):
        self.descricao = descricao
        self.valor = valor
    
    def __repr__(self):
        return f"{self.__class__.__name__}(descricao={self.descricao!r}, valor={self.valor!r})"
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, value):
        if not value or value < 0:
            raise ValorRendimentoInvalidoException("Valor do rendimento inválido! Digite um valor válido!")
        self._valor = value
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, value):
        if not value:
            raise DescricaoEmBrancoException("Descrição do rendimento em branco! Digite uma descrição válida!")
        self._descricao = value
    
    def CalculaRendimento(self):
        return self.valor
```

É observável que o código foi reescrito para usar _properties_, evitando a necessidade de métodos _get_ e _set_ separados para cada propriedade. Além disso, há a utilização da função __repr__ para exibir uma representação mais clara do objeto. Tais alterações fizeram o código tornar-se mais elegante e _pythônico_, sendo mais coeso, simples e de acordo com as convenções da linguagem.
