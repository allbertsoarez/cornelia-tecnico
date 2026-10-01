### 5. Tomando Decisões (Condicionais)
Neste módulo, o programa ganha "inteligência". Aprendemos a fazer o código executar caminhos diferentes dependendo de condições lógicas.

- **5.1 [Operadores Comparativos](https://docs.python.org/pt-br/3/library/stdtypes.html#comparisons)**: 
  Usados para comparar dois valores. O resultado é sempre um booleano (`True` ou `False`):
  - `==` (Igual a) → *Cuidado: não confundir com `=`, que é atribuição!*
  - `!=` (Diferente de)
  - `>` (Maior que), `>=` (Maior ou igual a)
  - `<` (Menor que), `<=` (Menor ou igual a)

- **5.2 [Operadores Lógicos](https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not)**: 
  Usados para combinar múltiplas condições:
  - `and`: Retorna `True` apenas se **todas** as condições forem verdadeiras.
  - `or`: Retorna `True` se **pelo menos uma** condição for verdadeira.
  - `not`: Inverte o valor lógico (`True` vira `False` e vice-versa).

- **5.3 [Estruturas Condicionais (if/elif/else)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements)**: 
  - `if`: "Se a condição for verdadeira, execute este bloco."
  - `elif`: "Senão, se esta outra condição for verdadeira, execute este bloco." (Pode ter vários `elif`.)
  - `else`: "Se nenhuma condição anterior for verdadeira, execute este bloco." (Opcional, e só pode haver um.)
  - **Indentação**: O Python usa espaços (4 espaços) para definir o que está "dentro" de cada bloco. Sem indentação correta, o código não roda (`IndentationError`).

- **5.4 [O Operador `in`](https://docs.python.org/pt-br/3/reference/expressions.html#membership-test-operations)**: 
  Verifica se um valor existe dentro de uma sequência (lista, string, tupla). Ex: `"a" in "banana"` retorna `True`.
  - **Listas vazias**: Uma lista vazia `[]` é avaliada como `False` em contextos booleanos. Isso permite verificar se uma lista tem itens com um simples `if minha_lista:`.
