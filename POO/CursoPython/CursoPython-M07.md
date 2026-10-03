### 7. [DICIONÁRIOS E SETS (MAPEAMENTOS E CONJUNTOS)](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
Neste módulo, saímos das sequências ordenadas (listas) e entramos no mundo dos mapeamentos e conjuntos matemáticos. 

- **[7.1 DICIONÁRIOS (`DICT`)](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries)**: 
  - A estrutura de pares **Chave-Valor**. A analogia da "ficha de cadastro" ou de uma função matemática $f(x)$, onde a chave é a entrada (domínio) e o valor é a saída (imagem).
  - Acessando, adicionando e modificando valores usando as chaves.

- **[7.2 MÉTODOS DE DICIONÁRIOS](https://docs.python.org/pt-br/3/library/stdtypes.html#mapping-types-dict)**: 
  - [`keys()`](https://docs.python.org/pt-br/3/library/stdtypes.html#dict.keys): Retorna todas as chaves.
  - [`values()`](https://docs.python.org/pt-br/3/library/stdtypes.html#dict.values): Retorna todos os valores.
  - [`items()`](https://docs.python.org/pt-br/3/library/stdtypes.html#dict.items): Retorna pares de (chave, valor), essencial para loops `for`.

- **[7.3 ANINHAMENTO DE DADOS](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries)**: 
  - A base dos bancos de dados NoSQL e APIs: Dicionários dentro de listas e listas dentro de dicionários.

- **[7.4 SETS (CONJUNTOS)](https://docs.python.org/pt-br/3/tutorial/datastructures.html#sets)**: 
  - Coleções **não ordenadas** que **não permitem elementos duplicados**.
  - **A "Mágica" dos Sets**: A forma mais rápida e elegante de remover duplicatas de uma lista (`lista_sem_duplicatas = list(set(lista))`).
  - **Operações Matemáticas**: [União (`|`)](https://docs.python.org/pt-br/3/library/stdtypes.html#set-types-set-frozenset), [Interseção (`&`)](https://docs.python.org/pt-br/3/library/stdtypes.html#set-types-set-frozenset) e [Diferença (`-`)](https://docs.python.org/pt-br/3/library/stdtypes.html#set-types-set-frozenset), aplicando a Teoria dos Conjuntos diretamente no código.

---

````mermaid
flowchart TD
    subgraph Dicionarios ["Dicionários: Mapeamento"]
        A["Chave (Domínio)"] -->|Mapeia para| B["Valor (Imagem)"]
        C["Métodos de Acesso"] -.-> D["keys()"]
        C -.-> E["values()"]
        C -.-> F["items() para loops"]
    end

    subgraph Sets ["Sets: Teoria dos Conjuntos"]
        G["Coleção não ordenada\nSem itens duplicados"] --> H["Elimina duplicatas de listas"]
        
        I["Conjunto A"] -->|União| J["A | B (Todos os elementos)"]
        I -->|Interseção| K["A & B (Elementos comuns)"]
        I -->|Diferença| L["A - B (Apenas em A)"]
        
        M["Conjunto B"] -.-> J
        M -.-> K
        M -.-> L
    end

    subgraph Estruturas ["Aninhamento de Dados"]
        N["Dicionários dentro de Listas"]
        O["Listas dentro de Dicionários"]
        N -.-> P["Estrutura base de APIs e JSON"]
        O -.-> P
    end
