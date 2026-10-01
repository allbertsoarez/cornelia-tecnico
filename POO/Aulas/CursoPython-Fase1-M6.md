### 6. A Arte da Repetição (Loops)
Neste módulo, automatizamos tarefas repetitivas. Em vez de escrever o mesmo código 100 vezes, ensinamos o computador a repetir um bloco de instruções de forma inteligente e controlada.

- **6.1 [Loop WHILE](https://docs.python.org/pt-br/3/reference/compound_stmts.html#the-while-statement)**: 
  - Executa um bloco de código **enquanto** uma condição for verdadeira.
  - **O Perigo do Loop Infinito**: A importância crucial de garantir que a condição eventualmente se torne `False`.
  - **Controles de Fluxo**: 
    - `break`: Interrompe o loop imediatamente, saindo dele.
    - `continue`: Pula o resto do bloco atual e volta para o início da próxima iteração.
  - **Flags**: O uso de variáveis booleanas (ex: `ativo = True`) para controlar o início e o fim de loops complexos.

- **6.2 [Loop FOR](https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements)**: 
  - Usado para iterar (percorrer) sequências de forma definida. É a escolha ideal quando sabemos quantas vezes queremos repetir algo ou quando queremos passar por cada item de uma coleção (lista, string, etc).
  - **A função `range()`**: A ferramenta mágica para gerar sequências numéricas. Sintaxe: `range(inicio, fim, passo)`. *Atenção: o valor do 'fim' nunca é incluído!*
