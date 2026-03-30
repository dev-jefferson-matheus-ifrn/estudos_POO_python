# Métodos de Classe em Python (@classmethod)

## Introdução

Em Programação Orientada a Objetos (POO) em Python, existem três tipos principais de métodos:

1. Métodos de instância
2. Métodos de classe
3. Métodos estáticos

Este documento foca nos **métodos de classe**.

---

## O que são Métodos de Classe?

Métodos de classe são métodos que operam sobre a **classe** em vez de operar sobre uma **instância (objeto)**.

Eles são definidos usando o decorator:

```python
@classmethod
```

E recebem como primeiro parâmetro:

```python
cls
```

* `self` → referência ao objeto
* `cls` → referência à classe

---

## Estrutura de um Método de Classe

```python
class MinhaClasse:
    
    atributo_classe = 0
    
    @classmethod
    def metodo_de_classe(cls, valor):
        cls.atributo_classe = valor
```

---

## Diferença entre os tipos de métodos

| Tipo de método | Primeiro parâmetro | Acessa                       |
| -------------- | ------------------ | ---------------------------- |
| Instância      | self               | Dados do objeto              |
| Classe         | cls                | Dados da classe              |
| Estático       | nenhum             | Não acessa classe nem objeto |

---

## Métodos de Instância vs Métodos de Classe

### Método de Instância

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_nome(self):
        return self.nome
```

Métodos de instância trabalham com os **dados do objeto**.

---

### Método de Classe

```python
class Pessoa:
    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

    @classmethod
    def mostrar_total_pessoas(cls):
        return cls.total_pessoas
```

Métodos de classe trabalham com **dados da classe**.

---

## Exemplo 1 – Alterando um atributo de classe

```python
class Produto:
    imposto = 0.1

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @classmethod
    def alterar_imposto(cls, novo_imposto):
        cls.imposto = novo_imposto
```

### Uso:

```python
Produto.alterar_imposto(0.2)

p1 = Produto("Notebook", 3000)
p2 = Produto("Mouse", 100)

print(Produto.imposto)
print(p1.imposto)
print(p2.imposto)
```

O imposto será alterado para **todos os objetos**, pois pertence à classe.

---

## Exemplo 2 – Método construtor alternativo

Métodos de classe são muito usados como **construtores alternativos**.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2026 - ano_nascimento
        return cls(nome, idade)
```

### Uso:

```python
p1 = Pessoa.criar_de_ano_nascimento("João", 2000)
print(p1.nome, p1.idade)
```

Aqui o método de classe cria um objeto sem chamar o construtor diretamente.

---

## Factory Methods (Métodos Fábrica)

Métodos de classe são frequentemente usados como **Factory Methods**, ou seja, métodos responsáveis por criar objetos.

```python
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @classmethod
    def criar_usuario_google(cls, nome):
        email = nome.lower() + "@gmail.com"
        return cls(nome, email)

    @classmethod
    def criar_usuario_empresa(cls, nome):
        email = nome.lower() + "@empresa.com"
        return cls(nome, email)
```

### Uso:

```python
u1 = Usuario.criar_usuario_google("Carlos")
u2 = Usuario.criar_usuario_empresa("Ana")

print(u1.email)
print(u2.email)
```

---

## Exemplo Prático – Conta Bancária

```python
class BankAccount:
    interest_rate = 0.05

    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    @classmethod
    def alter_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @classmethod
    def create_account_with_bonus(cls, holder):
        return cls(holder, 100)
```

### Uso:

```python
BankAccount.alter_interest_rate(0.1)

acc1 = BankAccount("João")
acc2 = BankAccount.create_account_with_bonus("Maria")

print(acc2.balance)
```

---

## Quando usar Métodos de Classe?

Use métodos de classe quando você precisar:

* Modificar atributos da classe
* Criar objetos de formas alternativas
* Criar fábricas de objetos
* Trabalhar com dados que pertencem à classe e não ao objeto
* Criar diferentes tipos de instâncias
* Contar quantos objetos foram criados
* Alterar configurações globais da classe

---

## Boas Práticas

* Use `cls` como nome padrão
* Métodos de classe geralmente são usados como **factory methods**
* Use quando o método precisa acessar ou modificar a classe
* Não use métodos de classe para lógica que depende do objeto
* Evite acessar atributos de instância dentro de métodos de classe

---

## Resumo

| Conceito                | Descrição                  |
| ----------------------- | -------------------------- |
| @classmethod            | Define um método de classe |
| cls                     | Referência para a classe   |
| Pode acessar            | Atributos de classe        |
| Pode criar objetos      | Sim                        |
| Pode modificar a classe | Sim                        |
| Pode ser factory method | Sim                        |

---

## Exercício Proposto

Crie uma classe `Car` com:

### Atributos:

* brand
* model
* year
* cars_created (atributo de classe)

### Métodos:

* Método de instância: exibir_dados()
* Método de classe: total_carros()
* Método de classe: criar_carro_padrao() → cria carro padrão (Fiat, Uno, 2020)

### Exemplo esperado:

```python
c1 = Car("Toyota", "Corolla", 2022)
c2 = Car.criar_carro_padrao()

print(Car.total_carros())
```
