### 8. Funções e Parâmetros
Neste módulo, damos o salto da programação procedural para a criação de ferramentas reutilizáveis. Aprendemos a aplicar o princípio DRY ("Don't Repeat Yourself") e a estruturar o código em blocos lógicos.

- **8.1 O Princípio DRY (Don't Repeat Yourself)**: 
  Se você está copiando e colando o mesmo bloco de código em vários lugares, você precisa de uma função. Funções centralizam a lógica: se houver um erro ou uma mudança na regra, você corrige em um único lugar.

- **8.2 Criando Funções (`def`) e o Retorno (`return`)**: 
  - A palavra-chave `def` define a função.
  - **A diferença crucial entre `print` e `return`**: `print` apenas exibe texto na tela para o humano ler. `return` devolve um valor para o programa, permitindo que esse valor seja guardado em uma variável e usado em cálculos futuros.

- **8.3 Parâmetros e Argumentos**: 
  - **Parâmetros**: As variáveis declaradas na definição da função (a "entrada" da função $f(x)$).
  - **Argumentos**: Os valores reais passados para a função quando a chamamos.
  - **Parâmetros com Valor Padrão**: Permitem que a função seja chamada sem fornecer todos os argumentos, usando um valor "default" se nenhum for especificado.
  - **Argumentos Nomeados (Keyword Arguments)**: Permitem passar os argumentos fora de ordem, especificando o nome do parâmetro (ex: `calcular(preco=100, desconto=0.1)`).
