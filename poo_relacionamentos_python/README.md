# Relacionamentos em Programação Orientada a Objetos (Python)

## Associação, Agregação e Composição

Na Programação Orientada a Objetos (POO), classes podem se relacionar entre si de diferentes formas.
Os três principais tipos de relacionamento são:

* Associação
* Agregação
* Composição

Esses relacionamentos representam como os objetos interagem e dependem uns dos outros.

---

# 1. Associação

## O que é Associação?

A **associação** é o relacionamento mais simples entre objetos.
Ela acontece quando **um objeto usa outro objeto**, mas **nenhum deles depende do outro para existir**.

É uma relação fraca.

### Exemplo conceitual:

* Professor usa um Livro
* Cliente faz um Pedido
* Pessoa usa um Carro

O objeto apenas **se relaciona** com o outro.

---

## Exemplo em Python – Associação

```python
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo


class Professor:
    def __init__(self, nome):
        self.nome = nome

    def usar_livro(self, livro):
        print(f"O professor {self.nome} está usando o livro {livro.titulo}")


livro1 = Livro("Python POO")
prof = Professor("Carlos")

prof.usar_livro(livro1)
```

### O que aconteceu aqui?

* O livro foi criado fora.
* O professor apenas usa o livro.
* Nenhum objeto depende do outro para existir.
* Isso é **Associação**.

---

# 2. Agregação

## O que é Agregação?

A **agregação** é um relacionamento onde **um objeto tem outro objeto**, porém **o objeto pode existir independentemente**.

É uma relação **"tem um"**, mas com **dependência fraca**.

### Exemplo conceitual:

* Time tem Jogadores
* Universidade tem Professores
* Departamento tem Funcionários

Se o time acabar, os jogadores ainda existem.

---

## Exemplo em Python – Agregação

```python
class Jogador:
    def __init__(self, nome):
        self.nome = nome


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def mostrar_jogadores(self):
        print(f"Time {self.nome}:")
        for jogador in self.jogadores:
            print(jogador.nome)


j1 = Jogador("João")
j2 = Jogador("Pedro")

time = Time("Time A")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)

time.mostrar_jogadores()
```

### Por que isso é agregação?

* Os jogadores foram criados fora do time.
* O time apenas armazena os jogadores.
* Se o time deixar de existir, os jogadores continuam existindo.
* Isso é **Agregação**.

---

# 3. Composição

## O que é Composição?

A **composição** é um relacionamento onde **um objeto é dono de outro objeto**.
O objeto interno **não existe sem o objeto principal**.

É uma relação **"tem um" com dependência forte**.

### Exemplo conceitual:

* Casa tem Quartos
* Carro tem Motor
* Computador tem Processador
* Pedido tem Itens

Se a casa for destruída, os quartos também deixam de existir.

---

## Exemplo em Python – Composição

```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # Composição

    def mostrar_carro(self):
        print("Modelo:", self.modelo)
        print("Potência do motor:", self.motor.potencia)


carro1 = Carro("Fusca", 100)
carro1.mostrar_carro()
```

### Por que isso é composição?

* O motor é criado dentro da classe Carro.
* O carro é dono do motor.
* O motor não existe sem o carro nesse sistema.
* Isso é **Composição**.

---

# Diferença entre Associação, Agregação e Composição

| Tipo       | Relação | Dependência |
| ---------- | ------- | ----------- |
| Associação | Usa     | Nenhuma     |
| Agregação  | Tem     | Fraca       |
| Composição | É dono  | Forte       |

---

# Resumo Geral

## Associação

Um objeto apenas usa o outro.

```python
professor.usar_livro(livro)
```

## Agregação

Um objeto tem outro, mas eles podem existir separados.

```python
time.adicionar_jogador(jogador)
```

## Composição

Um objeto é dono do outro e cria ele dentro da classe.

```python
self.motor = Motor()
```

---

# Regra para nunca mais esquecer

Use essa lógica:

| Pergunta                                             | Tipo       |
| ---------------------------------------------------- | ---------- |
| Um objeto usa o outro?                               | Associação |
| Um objeto tem o outro, mas ele pode existir sozinho? | Agregação  |
| Um objeto é dono do outro e ele não existe sozinho?  | Composição |