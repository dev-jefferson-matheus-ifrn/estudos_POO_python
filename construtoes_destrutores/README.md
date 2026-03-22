# ⚙️ Construtores e Destrutores em Python

## 📌 O que são?

Em Programação Orientada a Objetos (POO), **construtores** e **destrutores** são métodos especiais usados para controlar o ciclo de vida de um objeto.

* **Construtor (`__init__`)**: executado automaticamente ao criar um objeto
* **Destrutor (`__del__`)**: executado quando o objeto é destruído

---

## 🏗️ Construtor (`__init__`)

O construtor é responsável por inicializar os atributos do objeto.

### 📌 Exemplo:

```python
class Cachorro:
    # Construtor da classe
    def __init__(self, name, race, weight, height):
        self.name = name
        self.race = race
        self.weight = weight
        self.height = height
        
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'
    
    def bark(self):
        return 'AU AU!'
    
    # Destrutor da classe
    def __del__(self):
        pass
    
    
caramelo = Cachorro("Manteiga", "Golden", 50.0, 1.0)
```

### 🧪 Uso:

```python
pessoa = Pessoa("João", 25)
pessoa.apresentar()
```

### 🔎 Explicação:

* `__init__` é chamado automaticamente ao criar o objeto
* Define os atributos iniciais
* Sempre recebe `self` como primeiro parâmetro

---

## 🧹 Destrutor (`__del__`)

O destrutor é chamado quando o objeto é removido da memória.

### 📌 Exemplo:

```python
class Arquivo:
    def __init__(self, nome):
        self.nome = nome
        print(f"Arquivo {self.nome} criado.")

    def __del__(self):
        print(f"Arquivo {self.nome} foi destruído.")
```

### 🧪 Uso:

```python
arq = Arquivo("dados.txt")

del arq  # força a destruição do objeto
```

---

## ⚠️ Importante sobre o destrutor

* O método `__del__` **não é garantido de ser chamado imediatamente**
* Depende do **coletor de lixo (Garbage Collector)** do Python
* Pode não ser executado ao encerrar o programa

👉 Por isso, **não é recomendado usar `__del__` para lógica crítica**

---

## 🔄 Ciclo de vida do objeto

1. Objeto é criado → `__init__` é executado
2. Objeto é utilizado
3. Objeto é removido → `__del__` pode ser executado

---

## 💡 Boas práticas

### ✔ Use o construtor para:

* Inicializar atributos
* Validar dados
* Preparar o objeto

---

### ❌ Evite usar o destrutor para:

* Salvar dados importantes
* Fechar conexões críticas

👉 Prefira usar:

```python
with open("arquivo.txt") as f:
    conteudo = f.read()
```

---

## 🚀 Exemplo prático completo

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        print("Conta criada com sucesso!")

    def __del__(self):
        print(f"Conta de {self.titular} encerrada.")

    def mostrar_saldo(self):
        print(f"Saldo: R${self.saldo}")
```

---

## 📚 Resumo

| Método     | Função              |
| ---------- | ------------------- |
| `__init__` | Inicializa o objeto |
| `__del__`  | Finaliza o objeto   |

---

## 🎯 Conclusão

Construtores são essenciais e amplamente usados em Python.
Destrutores existem, mas devem ser utilizados com cautela devido ao comportamento do gerenciamento de memória.

---
