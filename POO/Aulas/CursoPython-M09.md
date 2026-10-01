### 9. Funções Avançadas e Módulos
Neste módulo, elevamos o nível das nossas funções, tornando-as extremamente flexíveis, e aprendemos a utilizar o vasto ecossistema de bibliotecas do Python.

- **9.1 Argumentos Arbitrários (`*args` e `**kwargs`)**: 
  - `*args`: Permite que uma função receba qualquer quantidade de argumentos posicionais. O Python os empacota em uma **tupla**.
  - `**kwargs`: Permite que uma função receba qualquer quantidade de argumentos nomeados (keyword arguments). O Python os empacota em um **dicionário**.

- **9.2 [Funções Anônimas (`lambda`)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#lambda-expressions)**: 
  - Funções de uma única linha, sem nome (`def`), úteis para operações rápidas e descartáveis.
  - Sintaxe: `lambda argumentos: expressão`.
  - Muito usadas em conjunto com funções como `sorted()`, `map()` e `filter()`.

- **9.3 [Módulos e Importações](https://docs.python.org/pt-br/3/tutorial/modules.html)**: 
  - O conceito de reutilização de código em escala. Um módulo é apenas um arquivo `.py` com funções e variáveis.
  - **Sintaxes de Importação**:
    - `import modulo`: Importa o módulo inteiro (acessa via `modulo.funcao()`).
    - `from modulo import funcao`: Importa apenas uma função específica (acessa via `funcao()`).
    - `import modulo as apelido`: Cria um apelido para o módulo (ex: `import numpy as np`).

- **9.4 Docstrings Profissionais**: 
  - A prática de documentar funções usando strings triple-quoted (`""" ... """`) logo após o `def`.
  - O que incluir: descrição, parâmetros (Args), retorno (Returns) e exemplos.
