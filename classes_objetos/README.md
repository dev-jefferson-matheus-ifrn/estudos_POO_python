# 🧠 Programação Orientada a Objetos (POO) em Python

## 📌 O que são Classes e Objetos?

A Programação Orientada a Objetos (POO) é um paradigma que organiza o código em estruturas chamadas **classes** e **objetos**.

* **Classe**: é um modelo (ou molde) para criar objetos
* **Objeto**: é uma instância de uma classe

---

## 🏗️ Definindo uma Classe

```python
# Criação da Classe Pessoa
class Pessoa:
    # Construtor em Python
    # self = Referência explicita para o objeto,Instancia do Objeto
    # self = Primeiro argumento explito
    def __init__(self,name,age):
        # Atributo para armazenar o nome
        self.name = name
        # Atributo par armazenar a idade
        self.age = age
        
    
    # Metodo para retornar uma apresentação
    def introduce_yourself(self):
        return f'Olá, meu nome é {self.name}!'
    
    
    # Metodo para exibir uma string persolanizada que representa o objeto
    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f'{key}={value}' for key, value in self.__dict__.items()])}'
    
```

### 🔎 Explicação:

* `__init__`: método construtor, executado ao criar o objeto
* `self`: referência ao próprio objeto
* `atributos`: `name`, `age`
* `métodos`: `introduce_yourself()`

---

## 👤 Criando Objetos

```python
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa1.introduce_yourself()
pessoa2.introduce_yourself()
```

---

