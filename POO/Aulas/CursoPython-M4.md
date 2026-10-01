### 4. Listas e Tuplas (Sequências Ordenadas)
Neste módulo, aprendemos a agrupar múltiplos valores em uma única variável, facilitando a manipulação de conjuntos de dados.

- **4.1 [Listas e Índices](https://docs.python.org/pt-br/3/tutorial/introduction.html#lists)**: 
  - O que são listas (delimitadas por colchetes `[]`).
  - Acessando itens: A regra de ouro de que a contagem começa no **ZERO** (`lista[0]`).
  - Índices negativos: O truque do `-1` para acessar o último item da lista.

- **4.2 [Métodos de Listas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists)**: 
  Ferramentas nativas para manipular a coleção:
  - **Adicionar**: `append()` (no final) e `insert()` (em uma posição específica).
  - **Remover**: `remove()` (por valor), `pop()` (por índice, retornando o item) e `del` (por índice).
  - **Organizar**: `sort()` (ordena a lista original) e `sorted()` (retorna uma nova lista ordenada).
  - **Medir**: `len()` (retorna a quantidade de itens).

- **4.3 Fatiamento (Slicing) e Cópia**: 
  - **Slicing**: A sintaxe `lista[inicio:fim]` para extrair sublistas.
  - **O perigo do `=`**: Entender que `lista_b = lista_a` não cria uma cópia, mas sim uma segunda referência para a mesma lista na memória. A forma correta de copiar é usar `lista_a.copy()`.

- **4.4 [Tuplas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples)**: 
  - Semelhantes às listas, mas delimitadas por parênteses `()`.
  - **A grande diferença**: São **imutáveis** (não podem ser alteradas após a criação).
  - **Quando usar**: Para dados que representam "registros" fixos, como dias da semana, coordenadas geográficas ou configurações que não devem mudar acidentalmente.
