## 🟢 [FASE 1: A FUNDAÇÃO (LÓGICA E SINTAXE BÁSICA)](https://docs.python.org/pt-br/3/tutorial/index.html)

### 2. [VARIÁVEIS, TIPOS E O "INPUT/OUTPUT"](https://docs.python.org/pt-br/3/tutorial/introduction.html)
Neste módulo, aprendemos como o computador armazena, classifica e recebe dados. É a base de qualquer interação entre o humano e a máquina.

- **[2.1 VARIÁVEIS E ATRIBUIÇÃO](https://docs.python.org/pt-br/3/tutorial/introduction.html)**: 
  A analogia da "caixa com rótulo" na memória. O uso do sinal de igual (`=`) não como uma igualdade matemática, mas como uma **atribuição** (o valor da direita é guardado na caixa da esquerda). A reatribuição (trocar o conteúdo da caixa) e a tipagem dinâmica (o Python descobre o tipo sozinho).

- **[2.2 TIPOS PRIMITIVOS](https://docs.python.org/pt-br/3/library/stdtypes.html)**: 
  Os 4 blocos de construção fundamentais:
  - `int`: Números inteiros.
  - `float`: Números decimais (usando ponto).
  - `str`: Textos (delimitados por aspas).
  - `bool`: Lógica binária (`True` ou `False`).
  - *Ferramenta essencial*: A função `type()` para descobrir a natureza de qualquer variável.

- **[2.3 ENTRADA E SAÍDA (INPUT/OUTPUT)](https://docs.python.org/pt-br/3/tutorial/inputoutput.html)**: 
  - `input()`: A forma de o programa fazer uma pergunta e pausar a execução até o usuário digitar algo e apertar Enter.
  - `print()`: A forma de o programa exibir respostas na tela.
  - **f-strings**: A sintaxe moderna (`f"Texto {variavel}"`) para misturar textos e variáveis de forma elegante.

- **[2.4 CONVERSÃO DE TIPOS (CASTING)](https://docs.python.org/pt-br/3/library/functions.html)**: 
  A "pegadinha" clássica do Python: a função `input()` **sempre** retorna um texto (`str`), mesmo que você digite um número. Para fazer matemática com esses dados, é obrigatório usar as funções de conversão `int()` (para inteiros) ou `float()` (para decimais), que são funções embutidas (*built-in*) da linguagem.
