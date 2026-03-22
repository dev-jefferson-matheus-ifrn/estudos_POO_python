# 🧬 Herança em Python (POO)

## 📌 O que é Herança?

Herança é um dos pilares da Programação Orientada a Objetos (POO) que permite que uma classe **herde atributos e métodos** de outra.

👉 Isso promove:

* Reutilização de código
* Organização
* Extensibilidade

---

## 🏗️ Classe Base (Superclasse)

A classe base é aquela que será herdada por outras classes.

```python
class Cliente:
    def __init__(self,country,data_register):
        self.country = country
        self.data_register = data_register
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'
        
```

---

## 🧬 Classe Derivadas (Subclasses)

A classe derivada herda da classe base.

```python
from cliente import Cliente

class Pessoa_fisica(Cliente):
    def __init__(self, country, data_register, name, last_name, cpf):
        super().__init__(country, data_register)
        
        self.name = name
        self.last_name = last_name
        self.cpf = cpf
```

```python
from cliente import Cliente

class Pessoa_juridica(Cliente):
    def __init__(self, country, data_register, social_reason, name_fantasy, acronym, cnpj):
        super().__init__(country, data_register)
        
        self.social_reason = social_reason
        self.name_fantasy = name_fantasy
        self.acronym = acronym
        self.cnpj = cnpj
```

---

## 🧪 Exemplo de uso

```python
from pessoa_fisica import Pessoa_fisica

from pessoa_juridica import Pessoa_juridica

cliente_fisico = Pessoa_fisica("Brasil", "10/11/2022", "João","da Silva", "111-222-333-44")

cliente_juridco = Pessoa_juridica("Brasil","10/11/2022","Juninho GamePlays","JG games", "JG", "99.999.999/9999-99")


print(cliente_fisico.__str__())
print("_______________________________")
print(cliente_juridco.__str__())
```

---

## 🔗 Usando `super()`

O `super()` permite acessar métodos da classe pai.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
```

---

## 🧠 Tipos de Herança

### 🔹 Herança Simples

```python
class A:
    pass

class B(A):
    pass
```

---

### 🔹 Herança Múltipla

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---


## ⚠️ Cuidados ao usar herança

* Não use herança sem necessidade
* Prefira quando houver relação **"é um" (is-a)**
* Evite heranças muito profundas

---

## 💡 Boas práticas

✔ Use nomes claros
✔ Reutilize código da classe base
✔ Use `super()` corretamente
✔ Sobrescreva métodos quando necessário

---

## 📚 Resumo

| Conceito    | Descrição                      |
| ----------- | ------------------------------ |
| Classe Base | Classe que é herdada           |
| Subclasse   | Classe que herda               |
| `super()`   | Acessa a classe pai            |

---

## 🚀 Conclusão

Herança permite criar sistemas mais organizados e reutilizáveis.
Quando bem aplicada, reduz duplicação de código e facilita manutenção.

---
