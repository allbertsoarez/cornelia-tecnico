### 6. [A ARTE DA REPETIÇÃO (LOOPS)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#more-on-loops)
Neste módulo, automatizamos tarefas repetitivas. Em vez de escrever o mesmo código 100 vezes, ensinamos o computador a repetir um bloco de instruções de forma inteligente e controlada.

- **[6.1 LOOP WHILE](https://docs.python.org/pt-br/3/reference/compound_stmts.html#the-while-statement)**: 
  - Executa um bloco de código **enquanto** uma condição for verdadeira.
  - **O Perigo do Loop Infinito**: A importância crucial de garantir que a condição eventualmente se torne `False`.
  - **Controles de Fluxo**: 
    - [`break`](https://docs.python.org/pt-br/3/reference/simple_stmts.html#break): Interrompe o loop imediatamente, saindo dele.
    - [`continue`](https://docs.python.org/pt-br/3/reference/simple_stmts.html#continue): Pula o resto do bloco atual e volta para o início da próxima iteração.
  - **Flags**: O uso de variáveis booleanas (ex: `ativo = True`) para controlar o início e o fim de loops complexos.

- **[6.2 LOOP FOR](https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements)**: 
  - Usado para iterar (percorrer) sequências de forma definida. É a escolha ideal quando sabemos quantas vezes queremos repetir algo ou quando queremos passar por cada item de uma coleção (lista, string, etc).
  - **A função [`range()`](https://docs.python.org/pt-br/3/library/stdtypes.html#range)**: A ferramenta mágica para gerar sequências numéricas. Sintaxe: `range(inicio, fim, passo)`. *Atenção: o valor do 'fim' nunca é incluído!* (Ótimo gancho para revisar os conceitos de intervalos matemáticos!).

---

````mermaid
flowchart TD
    subgraph Inicio ["Início do Loop"]
        A["Avalia a Condição (while)\nou Próximo Item (for)"]
    end

    subgraph Decisao ["Decisão de Fluxo"]
        A --> B{"Condição Verdadeira\nou Item Disponível?"}
        B -->|Não| C["Sai do Loop\nFim da repetição"]
        B -->|Sim| D["Executa o Bloco de Código\nIndentação obrigatória"]
    end

    subgraph Controles ["Controles de Fluxo Internos"]
        D --> E{"Encontrou comando especial?"}
        E -->|Sim, break| F["Interrompe o loop\nimediatamente"]
        E -->|Sim, continue| G["Pula para a próxima\niteração"]
        E -->|Não| H["Fim normal da iteração"]
    end

    subgraph Fim ["Continuação do Programa"]
        F --> C
        G --> A
        H --> A
        C --> I["Próximas linhas de código\napós o loop"]
    end
