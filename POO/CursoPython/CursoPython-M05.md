### 5. [TOMANDO DECISÕES (CONDICIONAIS)](https://docs.python.org/pt-br/3/tutorial/controlflow.html)
Neste módulo, o programa ganha "inteligência". Aprendemos a fazer o código executar caminhos diferentes dependendo de condições lógicas.

- **[5.1 OPERADORES COMPARATIVOS](https://docs.python.org/pt-br/3/library/stdtypes.html#comparisons)**: 
  Usados para comparar dois valores. O resultado é sempre um booleano (`True` ou `False`):
  - `==` (Igual a) → *Cuidado: não confundir com `=`, que é atribuição!*
  - `!=` (Diferente de)
  - `>` (Maior que), `>=` (Maior ou igual a)
  - `<` (Menor que), `<=` (Menor ou igual a)

- **[5.2 OPERADORES LÓGICOS](https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not)**: 
  Usados para combinar múltiplas condições:
  - `and`: Retorna `True` apenas se **todas** as condições forem verdadeiras.
  - `or`: Retorna `True` se **pelo menos uma** condição for verdadeira.
  - `not`: Inverte o valor lógico (`True` vira `False` e vice-versa).

- **[5.3 ESTRUTURAS CONDICIONAIS (IF/ELIF/ELSE)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements)**: 
  - `if`: "Se a condição for verdadeira, execute este bloco."
  - `elif`: "Senão, se esta outra condição for verdadeira, execute este bloco." (Pode ter vários `elif`.)
  - `else`: "Se nenhuma condição anterior for verdadeira, execute este bloco." (Opcional, e só pode haver um.)
  - **Indentação**: O Python usa espaços (4 espaços por nível) para definir o que está "dentro" de cada bloco. Sem a indentação correta, o código não roda e gera um [`IndentationError`](https://docs.python.org/pt-br/3/tutorial/errors.html#indentationerror).

- **[5.4 O OPERADOR `IN` (TESTES DE PERTINÊNCIA)](https://docs.python.org/pt-br/3/reference/expressions.html#membership-test-operations)**: 
  Verifica se um valor existe dentro de uma sequência (lista, string, tupla). Ex: `"a" in "banana"` retorna `True`.
  - **Listas vazias**: Uma lista vazia `[]` é avaliada como `False` em contextos booleanos (é considerada "falsy"). Isso permite verificar se uma lista tem itens de forma pythonica, com um simples `if minha_lista:`.

---

````mermaid
flowchart TD
    subgraph Entrada ["Avaliação Inicial"]
        A["Variável ou Expressão\n(ex: nota, 'a' in texto, minha_lista)"]
    end

    subgraph Condicional ["Estrutura de Decisão"]
        A --> B{"Condição 1 é verdadeira?\n(ex: nota >= 7)"}
        
        B -->|Sim| C["Executa Bloco IF\n(Indentação de 4 espaços obrigatória)"]
        B -->|Não| D{"Condição 2 é verdadeira?\n(ex: elif nota >= 5)"}
        
        D -->|Sim| E["Executa Bloco ELIF\n(Pode haver vários blocos elif)"]
        D -->|Não| F["Executa Bloco ELSE\n(Caminho padrão, opcional)"]
    end

    subgraph Conclusao ["Continuação do Programa"]
        C --> G["Fim da Estrutura Condicional"]
        E --> G
        F --> G
        G --> H["Próximas linhas de código executadas"]
    end

