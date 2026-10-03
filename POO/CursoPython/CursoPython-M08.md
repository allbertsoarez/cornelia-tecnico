### 8. [FUNÇÕES E PARÂMETROS](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions)
Neste módulo, damos o salto da programação procedural para a criação de ferramentas reutilizáveis. Aprendemos a aplicar o princípio DRY ("Don't Repeat Yourself") e a estruturar o código em blocos lógicos.

- **[8.1 O PRINCÍPIO DRY (DON'T REPEAT YOURSELF)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions)**: 
  Se você está copiando e colando o mesmo bloco de código em vários lugares, você precisa de uma função. Funções centralizam a lógica: se houver um erro ou uma mudança na regra, você corrige em um único lugar.

- **[8.2 CRIANDO FUNÇÕES (`DEF`) E O RETORNO (`RETURN`)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions)**: 
  - A palavra-chave [`def`](https://docs.python.org/pt-br/3/reference/compound_stmts.html#function-definitions) define a função.
  - **A diferença crucial entre `print` e [`return`](https://docs.python.org/pt-br/3/reference/simple_stmts.html#the-return-statement)**: `print` apenas exibe texto na tela para o humano ler. `return` devolve um valor para o programa, permitindo que esse valor seja guardado em uma variável e usado em cálculos futuros.

- **[8.3 PARÂMETROS E ARGUMENTOS](https://docs.python.org/pt-br/3/tutorial/controlflow.html#more-on-defining-functions)**: 
  - **Parâmetros**: As variáveis declaradas na definição da função (a "entrada" da função $f(x)$).
  - **Argumentos**: Os valores reais passados para a função quando a chamamos.
  - **[Parâmetros com Valor Padrão](https://docs.python.org/pt-br/3/tutorial/controlflow.html#default-argument-values)**: Permitem que a função seja chamada sem fornecer todos os argumentos, usando um valor "default" se nenhum for especificado.
  - **[Argumentos Nomeados (Keyword Arguments)](https://docs.python.org/pt-br/3/tutorial/controlflow.html#keyword-arguments)**: Permitem passar os argumentos fora de ordem, especificando o nome do parâmetro (ex: `calcular(preco=100, desconto=0.1)`).
