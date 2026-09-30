# 📘 MINI CURSO DE PYTHON

Bem-vindo ao guia de estudos teóricos do nosso Mini Curso! 
Este documento foi criado para ser sua bússola conceitual. Aqui você encontrará explicações claras e diretas sobre cada tópico. A recomendação é: **leia o conceito aqui** para entender a lógica e, em seguida, **abra o Notebook correspondente no Google Colab** para praticar.

Lembre-se: programação se aprende lendo a teoria, mas se consolida digitando, errando e corrigindo o código!

---

### 1. [ENTRADA/SAÍDA](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#)
É a forma como o programa "conversa" com o mundo exterior. Os tópicos centrais desta seção são:

1.1 **Função [input()](https://docs.python.org/pt-br/3/builtins/functions.html#input)**: Recebe dados digitados pelo usuário. *Atenção: no Python, o `input` sempre retorna um texto (`str`), mesmo que o usuário digite um número.*

1.2 **Função [print()](https://docs.python.org/pt-br/3/builtins/functions.html#print)**: Exibe informações, variáveis e resultados na tela do console.

1.3 **[f-strings](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#tut-f-strings)**: A forma moderna e recomendada de formatar a saída, permitindo inserir variáveis e expressões diretamente dentro do texto de forma limpa (ex: `f"Olá, {nome}"`).

---

### 2. VARIÁVEIS
São como "caixas com rótulos" na memória do computador onde guardamos informações para usar depois. Os tópicos centrais desta seção são:

2.1 **Atribuição**: O uso do sinal de igual (`=`) para guardar um valor dentro da variável (ex: `idade = 20`).

2.2 **Tipagem Dinâmica**: O Python descobre automaticamente o tipo de dado da variável, não sendo necessário declará-lo explicitamente antes de usá-la.

2.3 **Nomes Semânticos**: A boa prática de usar nomes que expliquem o conteúdo da variável (ex: `nota_do_aluno` em vez de apenas `x` ou `n`), tornando o código legível.

2.4 **Regras de Nomeação**: Nomes de variáveis devem começar com letra ou underline (`_`), não podem conter espaços, e não podem ser palavras reservadas da linguagem (como `if`, `for`, `class`).

---

### 3. TIPOS DE DADOS PRIMITIVOS
São os blocos de construção mais básicos da linguagem:
  
  - **3.1 [int](https://docs.python.org/pt-br/3/builtins/functions.html#int)**: Números inteiros, positivos ou negativos, sem casas decimais (ex: `10`, `-5`).
  
  - **3.2 [float](https://docs.python.org/pt-br/3/builtins/functions.html#float)**: Números de ponto flutuante (decimais). *Atenção: em Python, usa-se ponto (`.`) e não vírgula (`,`) para separar as casas decimais* (ex: `3.14`, `9.5`).
  
  - **3.3 [bool](https://docs.python.org/pt-br/3/builtins/functions.html#bool)**: Tipo lógico que representa apenas dois estados: `True` (Verdadeiro) ou `False` (Falso). Fundamental para tomadas de decisão.

---

### 4. OPERADORES ARITMÉTICOS
Utilizados para realizar operações matemáticas:
  
  - **4.1 SOMA (+)**: Adiciona dois valores. Também concatena (junta) textos.
  
  - **4.2 SUBTRAÇÃO (-)**: Subtrai o segundo valor do primeiro.
  
  - **4.3 MULTIPLICAÇÃO (*)**: Multiplica dois valores. Também repete textos (ex: `"A" * 3` vira `"AAA"`).
  
  - **4. DIVISÃO (/)**: Divide dois valores e sempre retorna um `float` (ex: `4 / 2` resulta em `2.0`).
  
  - **4.5 RESTO DA DIVISÃO / MÓDULO (%)**: Retorna o resto da divisão inteira (ex: `5 % 2` resulta em `1`). Muito útil para saber se um número é par ou ímpar.
  
  - **4.6 DIVISÃO INTEIRA (//)**: Divide e descarta a parte decimal, retornando apenas a parte inteira do resultado (ex: `5 // 2` resulta em `2`).
  
  - **4.7 EXPONENCIAÇÃO (**)**: Eleva um número à potência de outro (ex: `2 ** 3` resulta em `8`).

---

### 5. [OPERADORES LÓGICOS (and, or, not)](https://docs.python.org/pt-br/3/builtins/stdtypes.html#boolean-operations-and-or-not)
Usados para combinar múltiplas condições booleanas:
  
  - **5.1 and**: Retorna `True` apenas se **todas** as condições forem verdadeiras.
  
  - **5.2 or**: Retorna `True` se **pelo menos uma** das condições for verdadeira.
  
  - **5.3 not**: Inverte o valor lógico (de `True` para `False`, e vice-versa).

---

### 6. [OPERADORES COMPARATIVOS (<, <=, >, >=, ==, !=)](https://docs.python.org/pt-br/3/builtins/stdtypes.html#comparisons)
Usados para comparar dois valores. O resultado de qualquer comparação é sempre um booleano (`True` ou `False`):
  
  - 6.1 `<` (Menor que), `<=` (Menor ou igual a)
  
  - 6.2 `>` (Maior que), `>=` (Maior ou igual a)
  
  - 6.3 `==` (Igual a) → *Cuidado: não confundir com `=`, que é usado para atribuição!*
  
  - 6.4 `!=` (Diferente de)

---

### 7. FUNÇÕES INTEGRADAS (built-in)
Ferramentas que o Python já traz prontas para uso, sem precisar importar nada:
  
  - 7.1 [`abs()`](https://docs.python.org/pt-br/3.14/builtins/functions.html#abs): Retorna o valor absoluto (módulo) de um número.
  
  - 7.2 [`max()`](https://docs.python.org/pt-br/3.14/builtins/functions.html#max) e [`min()`](https://docs.python.org/pt-br/3.14/builtins/functions.html#min): Retornam o maior e o menor valor de uma sequência, respectivamente.
  
  - 7.3 [`sum()`](https://docs.python.org/pt-br/3.14/builtins/functions.html#sum): Retorna a soma de todos os itens de uma sequência numérica.
  
  - 7.4 [`type()`](https://docs.python.org/pt-br/3.14/builtins/functions.html#type)(: Revela qual é o tipo de dado de uma variável (ex: `<class 'int'>`).

---

### 8. FLUXO DE CONTROLE (if, elif, else, while)
Permite que o programa tome decisões e repita ações.
  
  - **8.1 if / elif / else**: Estruturas condicionais. O código executa blocos diferentes dependendo se uma condição é verdadeira ou falsa.
  
  - **8.2 while**: Repete um bloco de código **enquanto** uma condição for verdadeira. É essencial saber definir uma "condição de parada" para evitar loops infinitos.
  
  - *Nota*: O Python usa **indentação** (espaços no início da linha) para definir o que está dentro desses blocos. A indentação é obrigatória e faz parte da sintaxe!

---

### 9. LAÇO For
Diferente do `while`, o `for` é usado para iterar (percorrer) sequências de forma definitiva. É ideal quando sabemos quantas vezes queremos repetir algo ou quando queremos passar por cada item de uma coleção. Frequentemente usamos a função `range(inicio, fim, passo)` para gerar sequências numéricas para o `for` percorrer.

---

### 10. LISTAS
Uma coleção ordenada e mutável de itens. Permitem guardar múltiplos valores em uma única variável (ex: `[10, 20, 30]`). Os itens são acessados por **índices**, e no Python a contagem começa sempre em **0**. Possuem métodos úteis como `.append()` (adicionar ao final) e `.pop()` (remover).

---

### 11. COLEÇÕES (str, lst, tuple, dict, set)
Uma visão geral das principais estruturas para agrupar dados:
  
  - **11.1 str (String)**: Sequência imutável de caracteres (textos).
  
  - **11.2 lst (List / Lista)**: Sequência ordenada e mutável (permite alterar, adicionar e remover itens).
  
  - **11.3 tuple (Tupla)**: Semelhante à lista, mas é **imutável** (não pode ser alterada após a criação). Usa parênteses `()`. Ótima para dados que não devem mudar.
  
  - **11.4 dict (Dicionário)**: Coleção de pares **Chave-Valor** (ex: `{"nome": "Ana", "idade": 20}`). A busca é feita pela chave, não por índice. É a base para entender Objetos no futuro.
  
  - **11.5 set (Conjunto)**: Coleção **não ordenada** e que **não permite elementos duplicados**. Excelente para remover duplicatas de uma lista ou fazer operações matemáticas de conjuntos (união, interseção).

---

### 🚀 PRÓXIMOS PASSOS
Agora que você revisou os conceitos teóricos, é hora de praticar! Acesse a pasta de Notebooks do Google Colab neste repositório e comece pelo **Módulo 0**. Boa jornada!
