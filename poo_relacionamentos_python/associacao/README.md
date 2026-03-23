# 📘 Associação em Programação Orientada a Objetos (Python)

## 📌 O que é Associação?

Associação é um tipo de relacionamento entre classes onde um objeto utiliza outro para realizar alguma funcionalidade.

Diferente de outros relacionamentos mais fortes, como composição ou agregação, na associação os objetos **podem existir independentemente**.

---

## 🧠 Conceito-chave

> Associação representa um relacionamento "usa" entre objetos.

Exemplo do mundo real:

* Um **Aluno** se associa a um **Curso**
* Um **Cliente** faz um **Pedido**
* Um **Professor** ensina vários **Alunos**

---

## 🔹 Tipos de Associação

### 1. Associação Simples (1 para 1)

Um objeto se relaciona com outro.

```python
class Curso:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.curso = None

    def matricular(self, curso):
        self.curso = curso
```

---

### 2. Associação 1 para Muitos

Um objeto se relaciona com vários outros.

```python
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
```

---

### 3. Associação Bidirecional

Ambos os objetos possuem referência um ao outro.

```python
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

class Pedido:
    def __init__(self, descricao, cliente):
        self.descricao = descricao
        self.cliente = cliente
        cliente.pedidos.append(self)
```

---

### 4. Associação por Dependência (uso em métodos)

Um objeto usa outro apenas para executar uma ação.

```python
class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self, motor):
        self.motor = motor

    def ligar(self):
        return self.motor.ligar()
```

---

## 🔍 Associação vs Outros Relacionamentos

| Tipo       | Descrição                       | Exemplo        |
| ---------- | ------------------------------- | -------------- |
| Associação | Relação fraca (uso)             | Aluno → Curso  |
| Agregação  | Relação "tem um" (independente) | Time → Jogador |
| Composição | Relação forte (dependência)     | Casa → Quarto  |

---

## 🧪 Boas Práticas

* Prefira associação quando não houver dependência forte
* Evite acoplamento excessivo entre classes
* Use nomes claros para atributos (ex: `cliente`, `motor`, `curso`)
* Utilize listas para representar múltiplas associações

---

## 🚀 Conclusão

Associação é um dos conceitos mais básicos e importantes da Programação Orientada a Objetos.

Ela permite criar sistemas mais flexíveis e desacoplados, facilitando manutenção e reutilização de código.

