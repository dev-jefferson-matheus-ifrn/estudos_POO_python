# 🔐 `@property`, Getters e Setters em Python

## 📌 O que são?

Em Programação Orientada a Objetos (POO), **getters** e **setters** são métodos usados para **acessar e modificar atributos de forma controlada**.

No Python, isso é feito de forma mais elegante com o uso do decorator `@property`.

---

## 🧠 Conceito principal

O `@property` permite que você:

> Use métodos como se fossem atributos

Isso cria uma interface mais limpa e segura para acessar dados.

---

## 🔧 Forma tradicional (sem `@property`)

```python
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
```

### Uso:

```python
conta = Conta(100)
conta.set_saldo(200)
print(conta.get_saldo())
```

---

## ✨ Usando `@property`

```python
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
```

### Uso:

```python
conta = Conta(100)
print(conta.saldo)
```

---

## 🔁 Setter com `@property`

```python
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
```

### Uso:

```python
conta = Conta(100)

conta.saldo = 200  # chama o setter
print(conta.saldo) # chama o getter
```

---

## 🔒 Atributos protegidos

Por convenção em Python:

* `_atributo` → protegido (uso interno)
* `atributo` → interface pública (via property)

---

## ❌ Somente leitura

Se você não definir um setter, o atributo se torna **somente leitura**:

```python
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco
```

```python
produto = Produto(50)
produto.preco = 100  # ❌ erro
```

---

## 🧹 Deleter (opcional)

Você também pode deletar um atributo com controle:

```python
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.deleter
    def saldo(self):
        del self._saldo
```

---

## ⚠️ Erros comuns

### 1. Recursão infinita

```python
@property
def saldo(self):
    return self.saldo  # ❌ errado
```

✔ Correto:

```python
return self._saldo
```

---

### 2. Chamar property como função

```python
self.saldo(100)  # ❌ errado
```

✔ Correto:

```python
self.saldo = 100
```

---

### 3. Misturar nomes

Errado:

```python
@property
def _saldo(self):
```

✔ Correto:

```python
@property
def saldo(self):
```

---

## 💡 Boas práticas

✔ Use `_atributo` para armazenamento interno
✔ Use `@property` para interface pública
✔ Sempre valide dados no setter
✔ Use o setter também no `__init__` quando necessário

---

## 📚 Resumo

| Recurso      | Função           |
| ------------ | ---------------- |
| `@property`  | Getter           |
| `@x.setter`  | Setter           |
| `@x.deleter` | Deletar atributo |

---

## 🚀 Conclusão

O uso de `@property` torna o código mais limpo, seguro e alinhado com as boas práticas de Python, substituindo os getters e setters tradicionais de forma elegante.

---
