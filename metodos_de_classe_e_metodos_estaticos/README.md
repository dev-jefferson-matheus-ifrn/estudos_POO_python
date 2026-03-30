# Métodos em Python: Instância vs Classe vs Estático

## Introdução

Em Programação Orientada a Objetos (POO) em Python, existem três tipos principais de métodos:

1. Métodos de instância
2. Métodos de classe (`@classmethod`)
3. Métodos estáticos (`@staticmethod`)

Entender a diferença entre eles é essencial para escrever código limpo e bem estruturado.

---

## Visão Geral

| Tipo de Método | Decorator       | Primeiro Parâmetro | Acessa               | Uso Principal                 |
| -------------- | --------------- | ------------------ | -------------------- | ----------------------------- |
| Instância      | nenhum          | `self`             | Objeto               | Trabalhar com dados do objeto |
| Classe         | `@classmethod`  | `cls`              | Classe               | Trabalhar com dados da classe |
| Estático       | `@staticmethod` | nenhum             | Nada automaticamente | Funções utilitárias           |

---

## Métodos de Instância

### O que são?

São métodos que operam sobre os **dados do objeto**.

### Exemplo:

```python id="o0y6fg"
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_nome(self):
        return self.nome
```

### Uso:

```python id="m4csd2"
p = Pessoa("João")
print(p.mostrar_nome())
```

---

## Métodos de Classe (@classmethod)

### O que são?

São métodos que operam sobre a **classe**, e não sobre instâncias específicas.

Recebem `cls` como parâmetro.

---

### Exemplo 1 – Alterando atributo de classe

```python id="mngnxb"
class Produto:
    imposto = 0.1

    @classmethod
    def alterar_imposto(cls, novo_imposto):
        cls.imposto = novo_imposto
```

### Uso:

```python id="nf7j4p"
Produto.alterar_imposto(0.2)
```

---

### Exemplo 2 – Factory Method

```python id="zhnujx"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_ano_nascimento(cls, nome, ano):
        idade = 2026 - ano
        return cls(nome, idade)
```

---

## Métodos Estáticos (@staticmethod)

### O que são?

São métodos que **não dependem nem da instância nem da classe**.

Funcionam como funções comuns, mas organizadas dentro da classe.

---

### Exemplo:

```python id="mfqkni"
class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b
```

### Uso:

```python id="7grumr"
Calculadora.somar(2, 3)
```

---

## Comparação Prática

```python id="36d8hg"
class Exemplo:

    valor = 10

    def metodo_instancia(self):
        return self.valor

    @classmethod
    def metodo_classe(cls):
        return cls.valor

    @staticmethod
    def metodo_estatico():
        return "Não depende da classe nem do objeto"
```

---

## Quando usar cada tipo?

### Use Método de Instância quando:

* Precisa acessar ou modificar dados do objeto
* Cada objeto pode ter valores diferentes

---

### Use Método de Classe quando:

* Precisa acessar ou modificar dados da classe
* Vai criar objetos de formas alternativas (factory methods)
* Quer compartilhar comportamento entre todas as instâncias

---

### Use Método Estático quando:

* Não precisa acessar `self` nem `cls`
* É uma função utilitária relacionada à classe
* Faz validações ou cálculos
* Quer organizar melhor o código

---

## Exemplo Completo (Misturando Tudo)

```python id="0y6m61"
class BankAccount:

    interest_rate = 0.05

    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, value):
        if self.valid_value(value):
            self.balance += value

    @classmethod
    def alter_interest_rate(cls, rate):
        cls.interest_rate = rate

    @classmethod
    def create_with_bonus(cls, holder):
        return cls(holder, 100)

    @staticmethod
    def valid_value(value):
        return value > 0
```

---

## Boas Práticas

* Use `self` para dados da instância
* Use `cls` para dados da classe
* Use `@staticmethod` para utilidades
* Prefira clareza ao invés de "forçar" uso de decorators
* Não use método de classe quando precisa de dados da instância
* Não use método estático se precisa acessar classe ou objeto

---

## Erros Comuns

### 1. Usar método estático quando precisa de `cls`

Errado:

```python id="46ofr0"
@staticmethod
def alterar_valor(valor):
    cls.valor = valor  # ERRO
```

---

### 2. Usar método de classe quando precisa de `self`

Errado:

```python id="pu0k6h"
@classmethod
def mostrar_nome(cls):
    return self.nome  # ERRO
```

---

### 3. Confundir criação de objetos com método de instância

Factory methods devem ser `@classmethod`, não métodos normais.

---

## Resumo Final

| Situação                           | Tipo de método ideal |
| ---------------------------------- | -------------------- |
| Trabalhar com dados do objeto      | Instância            |
| Trabalhar com dados da classe      | Classe               |
| Função auxiliar                    | Estático             |
| Criar objetos de forma alternativa | Classe               |
| Validação de dados                 | Estático             |


---

## Conclusão

* Métodos de instância trabalham com **objetos**
* Métodos de classe trabalham com **classes**
* Métodos estáticos são **funções utilitárias**

Dominar isso é essencial para escrever código orientado a objetos limpo e profissional.
