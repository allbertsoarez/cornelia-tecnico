### 📝 ATIVIDADE: VERIFICANDO TIPOS DE DADOS COM `type()`

**Contexto:**
Você precisa criar um programa no Google Colab que declare diferentes tipos de variáveis e exiba na tela o tipo de cada uma usando a função `type()`.

**Sua Missão:**
Criar uma célula no Google Colab que:
1. Declare variáveis de diferentes tipos (número inteiro, número decimal, texto e valor verdadeiro/falso)
2. Exiba na tela o valor de cada variável e seu respectivo tipo

---

### 🎯 O que você deve fazer

1. Crie uma **única célula** com o código que:
   - Declare uma variável com um número inteiro (ex: idade)
   - Declare uma variável com um número decimal (ex: altura)
   - Declare uma variável com um texto (ex: nome)
   - Declare uma variável com um valor verdadeiro ou falso (ex: estudante)
   - Exiba na tela cada variável e seu tipo usando `type()`
2. Execute a célula e observe os resultados

---

### 📋 Resultado Esperado

O resultado na tela deve mostrar algo como:

```
Idade: 25
Tipo: <class 'int'>

Altura: 1.75
Tipo: <class 'float'>

Nome: Maria
Tipo: <class 'str'>

Estudante: True
Tipo: <class 'bool'>
```

---

### 📊 O que você deve entregar

No seu arquivo do Colab, você deve ter:

1. **Célula 1 (código):** Código que declara as variáveis e exibe seus tipos
2. **Célula 2 (texto):** Explicação do que é cada tipo de dado (int, float, str, bool) e quando usamos cada um

---

### 📋 Critérios de Avaliação

| Critério                                  | Pontos  |
| :---------------------------------------- | :------ |
| Declarou variável do tipo inteiro (int)   | 1,0     |
| Declarou variável do tipo decimal (float) | 1,0     |
| Declarou variável do tipo texto (str)     | 1,0     |
| Declarou variável do tipo booleano (bool) | 1,0     |
| Usou a função `type()` corretamente       | 2,0     |
| Explicou corretamente cada tipo de dado   | 2,0     |
| **TOTAL**                                 | **8,0** |

---

### 🌟 Desafio Bônus (+2,0 pontos)

Crie uma variável com o resultado de uma operação matemática (ex: soma de duas variáveis) e exiba o tipo do resultado. O tipo mudou? Por que isso acontece?

---

### 🗝️ Gabarito (para o professor)

**Célula 1 (solução esperada):**
```python
idade = 25
altura = 1.75
nome = "Maria"
estudante = True

print(f"Idade: {idade}")
print(f"Tipo: {type(idade)}")
print()

print(f"Altura: {altura}")
print(f"Tipo: {type(altura)}")
print()

print(f"Nome: {nome}")
print(f"Tipo: {type(nome)}")
print()

print(f"Estudante: {estudante}")
print(f"Tipo: {type(estudante)}")
```

**Célula 2 (explicação esperada):**
O aluno deve explicar que:
- `int` (inteiro): números sem casas decimais (ex: 1, 25, -10)
- `float` (decimal): números com casas decimais (ex: 1.5, 3.14, -2.7)
- `str` (string): textos, sempre entre aspas (ex: "Maria", 'Python')
- `bool` (booleano): valores verdadeiro ou falso (True ou False)
