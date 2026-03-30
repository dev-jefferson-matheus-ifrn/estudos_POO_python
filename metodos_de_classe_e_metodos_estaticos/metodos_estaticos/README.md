# Métodos Estáticos em Python (@staticmethod)

## Introdução

Em Programação Orientada a Objetos (POO) em Python, existem três tipos de métodos:

1. Métodos de instância
2. Métodos de classe (@classmethod)
3. Métodos estáticos (@staticmethod)

Este documento foca nos **métodos estáticos**.

---

## O que são Métodos Estáticos?

Métodos estáticos são métodos que **não dependem da instância nem da classe**.

Eles funcionam como funções comuns, mas ficam **dentro da classe por organização**.

São definidos usando o decorator:

```python
@staticmethod
```

Diferente dos outros métodos:

* Não recebem `self`
* Não recebem `cls`

---

## Estrutura de um Método Estático

```python
class MinhaClasse:

    @staticmethod
    def meu_metodo():
        print("Método estático")
```

Uso:

```python
MinhaClasse.meu_metodo()
```

---

## Diferença entre os Tipos de Métodos

| Tipo de método | Recebe | Pode acessar         |
| -------------- | ------ | -------------------- |
| Instância      | self   | Atributos do objeto  |
| Classe         | cls    | Atributos da classe  |
| Estático       | nada   | Nada automaticamente |

---

## Quando usar Métodos Estáticos?

Use métodos estáticos quando:

* A função não precisa acessar atributos da classe
* A função não precisa acessar atributos do objeto
* É uma função utilitária relacionada à classe
* Você quer organizar melhor o código
* A função faz validações
* A função faz cálculos

---

## Exemplo 1 – Classe com Método Estático

```python
class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def multiplicar(a, b):
        return a * b
```

Uso:

```python
print(Calculadora.somar(5, 3))
print(Calculadora.multiplicar(4, 2))
```

Note que não precisamos criar um objeto.

---

## Exemplo 2 – Validação de Dados

```python
class Pessoa:

    def __init__(self, nome, idade):
        if Pessoa.validar_idade(idade):
            self.nome = nome
            self.idade = idade
        else:
            print("Idade inválida")

    @staticmethod
    def validar_idade(idade):
        return 0 <= idade <= 120
```

Uso:

```python
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 200)
```

Métodos estáticos são muito usados para **validações**.

---

## Exemplo 3 – Classe Banco

```python
class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        if BankAccount.valid_value(value):
            self.balance += value

    @staticmethod
    def valid_value(value):
        return value > 0
```

Aqui o método estático é usado para validar valores.

---

## Comparação Prática

```python
class Exemplo:

    class_attribute = 10

    def metodo_instancia(self):
        return self.class_attribute

    @classmethod
    def metodo_classe(cls):
        return cls.class_attribute

    @staticmethod
    def metodo_estatico():
        return "Não acessa nada da classe"
```

---

## Boas Práticas

* Use métodos estáticos para funções utilitárias
* Use quando o método não precisa acessar `self` nem `cls`
* Ajuda a organizar o código
* Evita criar funções soltas fora da classe
* Muito usado para validações e cálculos

---

## Resumo

| Método    | Usa  | Para que serve                |
| --------- | ---- | ----------------------------- |
| Instância | self | Trabalhar com dados do objeto |
| Classe    | cls  | Trabalhar com dados da classe |
| Estático  | nada | Funções utilitárias           |

---


## Conclusão

Métodos estáticos são usados quando uma função:

* Pertence conceitualmente à classe
* Não precisa acessar atributos do objeto
* Não precisa acessar atributos da classe
* Serve como função auxiliar
* Ajuda na organização do código

Eles são basicamente **funções dentro da classe**.
