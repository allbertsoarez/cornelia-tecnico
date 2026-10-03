### 9. [FUNÇÕES AVANÇADAS E MÓDULOS](https://docs.python.org/pt-br/3/tutorial/modules.html)
Neste módulo, elevamos o nível das nossas funções, tornando-as extremamente flexíveis, e aprendemos a utilizar o vasto ecossistema de bibliotecas do Python.

- **[9.1 ARGUMENTOS ARBITRÁRIOS (`*ARGS` E `**KWARGS`)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#arbitrary-argument-lists)**: 
  - `*args`: Permite que uma função receba qualquer quantidade de argumentos posicionais. O Python os empacota em uma **tupla**.
  - `**kwargs`: Permite que uma função receba qualquer quantidade de argumentos nomeados (keyword arguments). O Python os empacota em um **dicionário**.

- **[9.2 FUNÇÕES ANÔNIMAS (`LAMBDA`)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#lambda-expressions)**: 
  - Funções de uma única linha, sem nome (`def`), úteis para operações rápidas e descartáveis.
  - Sintaxe: `lambda argumentos: expressão`.
  - Muito usadas em conjunto com funções de alta ordem como [`sorted()`](https://docs.python.org/pt-br/3/library/functions.html#sorted), [`map()`](https://docs.python.org/pt-br/3/library/functions.html#map) e [`filter()`](https://docs.python.org/pt-br/3/library/functions.html#filter).

- **[9.3 MÓDULOS E IMPORTAÇÕES](https://docs.python.org/pt-br/3/tutorial/modules.html)**: 
  - O conceito de reutilização de código em escala. Um módulo é apenas um arquivo `.py` com funções e variáveis.
  - **Sintaxes de Importação**:
    - `import modulo`: Importa o módulo inteiro (acessa via `modulo.funcao()`).
    - `from modulo import funcao`: Importa apenas uma função específica (acessa via `funcao()`).
    - `import modulo as apelido`: Cria um apelido para o módulo (ex: `import numpy as np`).

- **[9.4 DOCSTRINGS PROFISSIONAIS](https://docs.python.org/pt-br/3/tutorial/controlflow.html#tut-docstrings)**: 
  - A prática de documentar funções usando strings triple-quoted (`""" ... """`) logo após o `def`.
  - O que incluir: descrição, parâmetros (Args), retorno (Returns) e exemplos (ótimo gancho para introduzir as boas práticas da [PEP 257](https://peps.python.org/pep-0257/)!).

---

````mermaid
flowchart TD
    subgraph Args ["Argumentos Arbitrários"]
        A["Múltiplos Argumentos na Chamada"] --> B{"Tipo do Argumento?"}
        B -->|Posicional| C["*args"]
        C --> D["Empacotado em Tupla"]
        B -->|Nomeado| E["**kwargs"]
        E --> F["Empacotado em Dicionário"]
    end

    subgraph Lambda ["Funções Anônimas"]
        G["Operação Rápida e Descartável"] --> H["Sintaxe: lambda arg: expressao"]
        H --> I["Aplicada em map, filter ou sorted"]
    end

    subgraph Modulos ["Estratégias de Importação"]
        J["Arquivo Python .py"] --> K["import modulo\nAcesso: modulo.funcao"]
        J --> L["from modulo import funcao\nAcesso direto: funcao"]
        J --> M["import modulo as apelido\nAcesso: apelido.funcao"]
    end

    subgraph Documentacao ["Boas Práticas"]
        N["Docstrings"] --> O["Triple aspas logo apos o def"]
        O --> P["Descreve Args, Returns e Exemplos\nPadrao PEP 257"]
    end
