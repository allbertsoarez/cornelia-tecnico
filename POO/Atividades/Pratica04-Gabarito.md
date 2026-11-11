### 🗝️ Gabarito - Atividade Pratica 04

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
- O aluno deve explicar que o `input()` sempre retorna uma string (texto), mesmo quando o usuário digita um número.
- Se tentarmos fazer cálculos matemáticos diretamente com o resultado do `input()`, o Python dá erro ou concatena textos em vez de somar números.
- Para resolver isso, precisamos converter a string para número usando `int()` (para inteiros) ou `float()` (para decimais).
