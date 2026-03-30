# Interfaces e Classes Abstratas em Python

## Introdução

Em Programação Orientada a Objetos (POO), **classes abstratas** e **interfaces** são usadas para definir **contratos** que outras classes devem seguir.

Elas ajudam a:

* Padronizar comportamentos
* Garantir consistência
* Facilitar manutenção e escalabilidade do código

Em Python, usamos o módulo:

```python
from abc import ABC, abstractmethod
```

---

## O que são Classes Abstratas?

Uma **classe abstrata** é uma classe que:

* Não pode ser instanciada diretamente
* Pode conter métodos abstratos e concretos
* Serve como base para outras classes

---

## Criando uma Classe Abstrata

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass
```

---

## O que são Métodos Abstratos?

Métodos abstratos são métodos que:

* Não possuem implementação
* Devem ser obrigatoriamente implementados nas subclasses

---

## Exemplo Básico

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):

    def fazer_som(self):
        return "Au Au"


class Gato(Animal):

    def fazer_som(self):
        return "Miau"
```

### Uso:

```python
c = Cachorro()
g = Gato()

print(c.fazer_som())
print(g.fazer_som())
```

---

## O que acontece se não implementar?

```python
class Passaro(Animal):
    pass

p = Passaro()  # ERRO
```

Erro:

```
TypeError: Can't instantiate abstract class Passaro with abstract method fazer_som
```

---

## Métodos Concretos em Classes Abstratas

Classes abstratas podem ter métodos normais também:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    def dormir(self):
        return "Dormindo..."

    @abstractmethod
    def fazer_som(self):
        pass
```

---

## Interfaces em Python

Python **não possui interfaces formais como Java**, mas podemos simular usando:

* Classes abstratas com apenas métodos abstratos

---

## Exemplo de Interface

```python
from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass
```

---

## Implementando Interface

```python
class CartaoCredito(Pagamento):

    def pagar(self, valor):
        return f"Pagamento de {valor} no crédito"


class Pix(Pagamento):

    def pagar(self, valor):
        return f"Pagamento de {valor} via PIX"
```

---

## Polimorfismo com Interfaces

```python
def processar_pagamento(pagamento, valor):
    print(pagamento.pagar(valor))


processar_pagamento(CartaoCredito(), 100)
processar_pagamento(Pix(), 50)
```

Aqui usamos **polimorfismo**, pois diferentes classes respondem ao mesmo método.

---

## Quando usar Classes Abstratas?

Use quando:

* Você quer definir uma estrutura base
* Algumas implementações são comuns
* Outras devem ser obrigatórias

---

## Quando usar Interfaces?

Use quando:

* Quer apenas definir um contrato
* Não precisa compartilhar implementação
* Quer garantir que classes tenham certos métodos

---

## Diferença: Classe Abstrata vs Interface

| Característica         | Classe Abstrata | Interface       |
| ---------------------- | --------------- | --------------- |
| Pode ter implementação | Sim             | Normalmente não |
| Pode ter atributos     | Sim             | Geralmente não  |
| Métodos obrigatórios   | Sim             | Sim             |
| Instanciação direta    | Não             | Não             |

---

## Exemplo Completo

```python
from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass


class Desenvolvedor(Funcionario):

    def calcular_bonus(self):
        return self.salario * 0.2


class Gerente(Funcionario):

    def calcular_bonus(self):
        return self.salario * 0.3
```

---

## Boas Práticas

* Use `ABC` para criar classes abstratas
* Use `@abstractmethod` para métodos obrigatórios
* Não instancie classes abstratas
* Use interfaces para definir contratos claros
* Prefira composição quando possível

---

## Erros Comuns

### 1. Esquecer de implementar método abstrato

```python
class Teste(Animal):
    pass  # ERRO ao instanciar
```

---

### 2. Tentar instanciar classe abstrata

```python
a = Animal()  # ERRO
```

---

### 3. Não usar ABC

```python
class Animal:
    @abstractmethod
    def fazer_som(self):
        pass
```

Isso não funciona corretamente sem herdar de `ABC`.

---


## Conclusão

* Classes abstratas definem **bases reutilizáveis**
* Interfaces definem **contratos**
* Ambos ajudam a criar código mais organizado e escalável
* São essenciais para projetos grandes e bem estruturados
