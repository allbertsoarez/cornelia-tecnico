### 4. [LISTAS E TUPLAS (SEQUÊNCIAS ORDENADAS)](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
Neste módulo, aprendemos a agrupar múltiplos valores em uma única variável, facilitando a manipulação de conjuntos de dados.

- **[4.1 LISTAS E ÍNDICES](https://docs.python.org/pt-br/3/library/stdtypes.html#lists)**: 
  - O que são listas (delimitadas por colchetes `[]`).
  - Acessando itens: A regra de ouro de que a contagem começa no **ZERO** (`lista[0]`).
  - Índices negativos: O truque do `-1` para acessar o último item da lista.

- **[4.2 MÉTODOS DE LISTAS](https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists)**: 
  Ferramentas nativas para manipular a coleção:
  - **Adicionar**: [`append()`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list.append) (no final) e [`insert()`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list.insert) (em uma posição específica).
  - **Remover**: [`remove()`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list.remove) (por valor), [`pop()`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list.pop) (por índice, retornando o item) e [`del`](https://docs.python.org/pt-br/3/reference/simple_stmts.html#the-del-statement) (por índice).
  - **Organizar**: [`sort()`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list.sort) (ordena a lista original) e [`sorted()`](https://docs.python.org/pt-br/3/library/functions.html#sorted) (retorna uma nova lista ordenada).
  - **Medir**: [`len()`](https://docs.python.org/pt-br/3/library/functions.html#len) (retorna a quantidade de itens).

- **[4.3 FATIAMENTO (SLICING) E CÓPIA](https://docs.python.org/pt-br/3/library/stdtypes.html#common-sequence-operations)**: 
  - **Slicing**: A sintaxe `lista[inicio:fim]` para extrair sublistas.
  - **O perigo do `=`**: Entender que `lista_b = lista_a` não cria uma cópia, mas sim uma segunda referência para a mesma lista na memória. A forma correta de copiar é usar [`lista_a.copy()`](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list.copy) ou o fatiamento completo `lista_a[:]`.

- **[4.4 TUPLAS](https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples)**: 
  - Semelhantes às listas, mas delimitadas por parênteses `()`.
  - **A grande diferença**: São **imutáveis** (não podem ser alteradas após a criação).
  - **Quando usar**: Para dados que representam "registros" fixos, como dias da semana, coordenadas geográficas (ótimo gancho para suas aulas de matemática!) ou configurações que não devem mudar acidentalmente.

 ---

````mermaid
flowchart TD
    subgraph Criacao ["Criação de Sequências"]
        A["Lista: delimitada por colchetes []"]
        B["Tupla: delimitada por parênteses ()"]
    end

    subgraph Mutabilidade ["Mutabilidade e Métodos"]
        A -->|É mutável| C["Permite: append, remove, sort, pop"]
        B -->|É imutável| D["Dados fixos, apenas leitura"]
    end

    subgraph Acesso ["Acesso e Fatiamento"]
        C --> E["Índices: começa no zero, menos um é o último"]
        D --> E
        E --> F["Fatiamento: extrair sublistas com inicio:fim"]
    end

    subgraph Copia ["O Perigo da Cópia"]
        G["Atribuição com igual: lista_b = lista_a"] -->|Gera referência| H["Alterar uma, altera a outra!"]
        I["Cópia real: lista_a.copy() ou lista_a[:]"] -->|Gera novo objeto| J["Listas independentes na memória"]
    end

