### 3. Manipulando Textos e Números
Neste módulo, aprendemos a "limpar" e transformar textos, e a dominar as operações matemáticas que o Python oferece, indo além da calculadora básica.

- **3.1 [Strings a fundo](https://docs.python.org/pt-br/3/tutorial/introduction.html#strings)**: 
  - **Concatenação**: Juntando textos com o operador `+`.
  - **Caracteres de Escape**: Usando `\n` para quebras de linha e `\t` para tabulações.
  - **Aspas e Barra Invertida**: Como usar aspas dentro de strings (alternando simples e duplas) e como escapar caracteres especiais com `\`.

- **3.2 [Métodos de Strings](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods)**: 
  Ferramentas nativas para manipular textos:
  - `strip()`, `lstrip()`, `rstrip()`: Removem espaços em branco nas pontas (essencial para limpar o `input` do usuário).
  - `upper()` e `lower()`: Convertem para maiúsculas e minúsculas.
  - `replace()`: Substitui partes de um texto.
  - `title()` e `capitalize()`: Formatação de nomes próprios.

- **3.3 [Números e Operadores Aritméticos](https://docs.python.org/pt-br/3/tutorial/introduction.html#numbers)**: 
  Além do básico (`+`, `-`, `*`, `/`), o Python possui operadores poderosos:
  - `**` (Exponenciação): Eleva um número à potência de outro.
  - `//` (Divisão Inteira): Divide e descarta a parte decimal.
  - `%` (Módulo/Resto): Retorna o resto da divisão (mágico para saber se um número é par/ímpar ou para criar ciclos).
  - **Precedência**: A ordem em que o Python resolve as contas (parênteses vêm primeiro!).

- **3.4 [Booleanos e Operadores Lógicos/Comparativos](https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not)**: 
  A base da tomada de decisão.
  - **Comparação**: `==` (igual), `!=` (diferente), `>`, `<`, `>=`, `<=`. O resultado é sempre `True` ou `False`.
  - **Lógica**: `and` (ambos verdadeiros), `or` (pelo menos um verdadeiro), `not` (inverte o valor).
