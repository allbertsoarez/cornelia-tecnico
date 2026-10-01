### 10. Introdução à POO (Classes e Objetos)
Neste módulo, damos o salto quântico da programação procedural para a Programação Orientada a Objetos. Aprendemos a modelar o mundo real no código, encapsulando dados e comportamentos em entidades coesas.

- **10.1 O Paradigma Orientado a Objetos**: 
  - A mudança de mentalidade: de "funções agindo sobre dados" para "dados com comportamentos próprios".
  - **Classe**: O "molde" ou "planta" que define a estrutura e o comportamento.
  - **Objeto (Instância)**: O "biscoito" ou "casa construída" a partir do molde. Uma entidade concreta criada a partir da classe.

- **10.2 O Método Construtor (`__init__`) e o `self`**: 
  - `__init__`: O método especial que é executado automaticamente quando um objeto é criado. Serve para inicializar os atributos.
  - `self`: Uma referência ao próprio objeto sendo criado. Permite que cada objeto tenha seus próprios atributos independentes.

- **10.3 Atributos de Instância**: 
  - Dados que pertencem a cada objeto individualmente. São definidos dentro do `__init__` usando `self.atributo = valor`.
  - Cada objeto tem sua própria cópia dos atributos.

- **10.4 Métodos de Instância**: 
  - Funções que pertencem à classe e podem acessar/modificar os atributos do objeto.
  - O primeiro parâmetro de qualquer método de instância é sempre `self`.
  - Permitem que o objeto "faça coisas" com seus próprios dados.
