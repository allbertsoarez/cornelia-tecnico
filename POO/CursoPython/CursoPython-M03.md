### 3. [MANIPULANDO TEXTOS E NÚMEROS](https://docs.python.org/pt-br/3/tutorial/introduction.html)
Neste módulo, aprendemos a "limpar" e transformar textos, e a dominar as operações matemáticas que o Python oferece, indo além da calculadora básica.

- **[3.1 STRINGS A FUNDO](https://docs.python.org/pt-br/3/tutorial/introduction.html#strings)**: 
  - **Concatenação**: Juntando textos com o operador `+`.
  - **Caracteres de Escape**: Usando `\n` para quebras de linha e `\t` para tabulações.
  - **Aspas e Barra Invertida**: Como usar aspas dentro de strings (alternando simples e duplas) e como escapar caracteres especiais com `\`.

- **[3.2 MÉTODOS DE STRINGS](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods)**: 
  Ferramentas nativas para manipular textos:
  - [`strip()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.strip), [`lstrip()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.lstrip), [`rstrip()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.rstrip): Removem espaços em branco nas pontas (essencial para limpar o `input` do usuário).
  - [`upper()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.upper) e [`lower()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.lower): Convertem para maiúsculas e minúsculas.
  - [`replace()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.replace): Substitui partes de um texto.
  - [`title()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.title) e [`capitalize()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.capitalize): Formatação de nomes próprios.

- **[3.3 NÚMEROS E OPERADORES ARITMÉTICOS](https://docs.python.org/pt-br/3/tutorial/introduction.html#numbers)**: 
  Além do básico (`+`, `-`, `*`, `/`), o Python possui operadores poderosos:
  - `**` (Exponenciação): Eleva um número à potência de outro.
  - `//` (Divisão Inteira): Divide e descarta a parte decimal.
  - `%` (Módulo/Resto): Retorna o resto da divisão (mágico para saber se um número é par/ímpar ou para criar ciclos).
  - **Precedência**: A ordem em que o Python resolve as contas (parênteses vêm primeiro!).

- **[3.4 BOOLEANOS E OPERADORES LÓGICOS/COMPARATIVOS](https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not)**: 
  A base da tomada de decisão.
  - **Comparação**: `==` (igual), `!=` (diferente), `>`, `<`, `>=`, `<=`. O resultado é sempre `True` ou `False`.
  - **Lógica**: `and` (ambos verdadeiros), `or` (pelo menos um verdadeiro), `not` (inverte o valor).

---
´´´´
flowchart TD
    subgraph Entrada [Entrada]
        A["Texto Bruto (ex: input)"]
    end

    subgraph Tratamento [Tratamento de Strings]
        A --> B["Limpeza: strip()"]
        B --> C["Padronizacao: lower() ou upper()"]
        C --> D["Texto Formatado e Seguro"]
    end

    subgraph Logica [Logica e Comparacao]
        D --> E{"Condicao Verdadeira?"}
        E -->|Sim (True)| F["Executa Acao"]
        E -->|Nao (False)| G["Ignora ou Trata Erro"]
    end

    subgraph Matematica [Operacoes Matematicas]
        H["Valores Numericos"] --> I["Basico: +, -, *, /"]
        I --> J["Avancado: ** (potencia), // (inteira), % (resto)"]
        J --> K["Resultado Numerico"]
    end
    
    F -.-> K
    ´´´
