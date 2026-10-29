### 📝 Atividade: Coletando Dados com `input()`

**Contexto:**
Você precisa criar um programa no Google Colab que peça informações ao usuário e exiba uma mensagem personalizada. Porém, há um detalhe importante: o `input()` sempre retorna texto, mesmo quando o usuário digita números!

**Sua Missão:**
Criar uma célula no Google Colab que:
1. Peça ao usuário o seu nome e a sua idade
2. Calcule em que ano o usuário fará 100 anos
3. Exiba uma mensagem personalizada com o resultado

---

### 🎯 O que você deve fazer

1. Crie uma **única célula** com o código que:
   - Use `input()` para pedir o nome do usuário
   - Use `input()` para pedir a idade do usuário
   - Calcule em que ano o usuário fará 100 anos
   - Exiba uma mensagem como: "Maria, você fará 100 anos em 2099!"
2. Teste o programa e observe o que acontece

---

### 📋 Resultado Esperado

O programa deve pedir os dados ao usuário e exibir algo como:

```
Qual é o seu nome? Maria
Qual é a sua idade? 25
Maria, você fará 100 anos em 2099!
```

---

### 📊 O que você deve entregar

No seu arquivo do Colab, você deve ter:

1. **Célula 1 (código):** Código que coleta os dados e exibe a mensagem
2. **Célula 2 (texto):** Explicação do problema que aconteceu ao tentar calcular com a idade e como você resolveu

---

### 📋 Critérios de Avaliação

| Critério | Pontos |
| :--- | :--- |
| Usou `input()` para coletar o nome | 1,0 |
| Usou `input()` para coletar a idade | 1,0 |
| Identificou o problema do tipo de dado retornado pelo `input()` | 2,0 |
| Converteu a idade para número corretamente | 2,0 |
| Calculou o ano corretamente | 1,0 |
| Exibiu a mensagem personalizada | 1,0 |
| **TOTAL** | **8,0** |

---

### 🌟 Desafio Bônus (+2,0 pontos)

Modifique o programa para pedir também o ano atual e calcular em quantos anos o usuário fará 100 anos (em vez de mostrar o ano). Use `input()` para o ano atual também.

---

### 🗝️ Gabarito (para o professor)

**Célula 1 (solução esperada):**
```python
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
ano_atual = 2026
anos_para_100 = 100 - idade
ano_100 = ano_atual + anos_para_100

print(f"{nome}, você fará 100 anos em {ano_100}!")
```

**Célula 2 (explicação esperada):**
O aluno deve explicar que o `input()` sempre retorna uma string (texto), mesmo quando o usuário digita um número. Se tentarmos fazer cálculos matemáticos diretamente com o resultado do `input()`, o Python dá erro ou concatena textos em vez de somar números. Para resolver isso, precisamos converter a string para número usando `int()` (para inteiros) ou `float()` (para decimais).
