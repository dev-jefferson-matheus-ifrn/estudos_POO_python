# 📘 Agregação em Programação Orientada a Objetos (POO) com Python

## 📌 O que é Agregação?

A **agregação** é um tipo de relacionamento entre classes na Programação Orientada a Objetos (POO), onde uma classe **utiliza ou possui referência a outra classe**, mas **sem assumir total controle sobre seu ciclo de vida**.

Em outras palavras:

> Na agregação, os objetos podem existir de forma independente.

---

## 🧠 Conceito Principal

* Representa uma relação **"tem um" (has-a)**.
* A classe "todo" contém ou usa objetos de outra classe.
* Os objetos agregados **não são destruídos** quando o objeto principal é destruído.

---

## 📊 Diferença entre Agregação e Composição

| Característica | Agregação                | Composição    |
| -------------- | ------------------------ | ------------- |
| Relação        | Fraca                    | Forte         |
| Ciclo de vida  | Independente             | Dependente    |
| Exemplo        | Professor → Departamento | Casa → Cômodo |
| Reutilização   | Alta                     | Baixa         |

---

## 🐍 Exemplo em Python

Vamos criar um exemplo simples com as classes `Departamento` e `Professor`.

### 🔹 Classe Departamento

```python
class Departamento:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_departamento(self):
        return f"Departamento: {self.nome}"
```

---

### 🔹 Classe Professor (Agregação)

```python
class Professor:
    def __init__(self, nome, departamento):
        self.nome = nome
        self.departamento = departamento  # Agregação

    def mostrar_info(self):
        return f"Professor: {self.nome}, {self.departamento.mostrar_departamento()}"
```

---

### 🔹 Uso das Classes

```python
# Criando um departamento (objeto independente)
departamento = Departamento("Ciência da Computação")

# Passando o departamento para o professor
professor = Professor("Carlos", departamento)

print(professor.mostrar_info())
```

---

## 🔍 Explicação do Exemplo

* O objeto `Departamento` é criado **fora** da classe `Professor`.
* O `Professor` apenas **recebe uma referência** ao `Departamento`.
* Se o `Professor` for deletado, o `Departamento` **continua existindo**.

---

## 📌 Vantagens da Agregação

* 🔁 Reutilização de código
* 🔓 Baixo acoplamento entre classes
* 🧩 Flexibilidade no design do sistema
* 🛠️ Facilita manutenção

---

## ⚠️ Quando Usar Agregação?

Use agregação quando:

* Um objeto **usa outro**, mas **não depende totalmente dele**
* Os objetos devem **existir independentemente**
* Você quer manter o sistema **mais desacoplado**

---

## 💡 Exemplo do Mundo Real

* Uma **Universidade** tem vários **Professores**
* Um **Time** tem vários **Jogadores**
* Um **Pedido** tem vários **Produtos**

👉 Em todos esses casos, os elementos podem existir sem o objeto principal.

---

## 🧾 Conclusão

A agregação é uma forma importante de modelar relacionamentos entre objetos na POO, permitindo criar sistemas mais flexíveis e reutilizáveis. Em Python, ela é facilmente implementada através da passagem de objetos como parâmetros.

---

## 📚 Referências

* Documentação oficial do Python: https://docs.python.org/3/
* Conceitos de POO clássicos (UML)

---
