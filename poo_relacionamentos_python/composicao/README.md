# Composição em Programação Orientada a Objetos (Python)

## O que é Composição?

A **composição** é um tipo de relacionamento da Programação Orientada a Objetos (POO) onde **uma classe contém objetos de outra classe como parte de sua estrutura**.

Esse relacionamento representa a ideia de **"tem um" (has-a)** e indica uma **dependência forte** entre os objetos.

Ou seja, **o objeto contido só existe por causa do objeto principal**.
Se o objeto principal for destruído, os objetos que fazem parte dele também deixam de existir.

---

## Exemplo Conceitual

Um exemplo clássico é:

* Um **Carro** tem um **Motor**
* Uma **Casa** tem **Quartos**
* Um **Computador** tem **Processador**, **Memória** e **Disco**

Esses elementos fazem parte do objeto principal, caracterizando **composição**.

---

## Composição em Python – Exemplo

```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print("Motor ligado")


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # Composição

    def ligar_carro(self):
        print(f"Carro {self.modelo} ligando...")
        self.motor.ligar()


carro1 = Carro("Fusca", 100)
carro1.ligar_carro()
```

### O que caracteriza a composição nesse exemplo?

* O objeto **Motor** é criado **dentro da classe Carro**.
* O **Carro é dono do Motor**.
* O Motor não foi criado fora e passado como parâmetro.
* Isso representa **composição**.

---


## Exemplo Mais Completo – Computador

```python
class Processador:
    def __init__(self, modelo):
        self.modelo = modelo


class Memoria:
    def __init__(self, tamanho):
        self.tamanho = tamanho


class Disco:
    def __init__(self, capacidade):
        self.capacidade = capacidade


class Computador:
    def __init__(self, modelo, proc, mem, disco):
        self.modelo = modelo
        self.processador = Processador(proc)
        self.memoria = Memoria(mem)
        self.disco = Disco(disco)

    def mostrar_configuracao(self):
        print("Computador:", self.modelo)
        print("Processador:", self.processador.modelo)
        print("Memória:", self.memoria.tamanho)
        print("Disco:", self.disco.capacidade)


pc = Computador("PC Gamer", "Intel i5", "16GB", "512GB SSD")
pc.mostrar_configuracao()
```

---

## Vantagens da Composição

* Melhor organização do código
* Classes menores e mais reutilizáveis
* Facilita manutenção
* Representa melhor o mundo real
* Evita heranças desnecessárias

---

## Resumo

A **composição** acontece quando:

* Uma classe **possui objetos de outra classe**
* Esses objetos são **criados dentro da classe principal**
* Existe uma **relação de dependência forte**
* Representa **"tem um"**
* Exemplo: Carro tem Motor, Computador tem Memória

---

## Regra prática para identificar composição

Se você puder falar:

> "Um objeto X tem um objeto Y"

Então provavelmente você está lidando com **composição**.
