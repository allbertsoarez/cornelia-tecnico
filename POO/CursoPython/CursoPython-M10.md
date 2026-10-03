### 10. [INTRODUÇÃO À POO (CLASSES E OBJETOS)](https://docs.python.org/pt-br/3/tutorial/classes.html)
Neste módulo, damos o salto quântico da programação procedural para a Programação Orientada a Objetos. Aprendemos a modelar o mundo real no código, encapsulando dados e comportamentos em entidades coesas.

- **[10.1 O PARADIGMA ORIENTADO A OBJETOS](https://docs.python.org/pt-br/3/tutorial/classes.html#classes)**: 
  - A mudança de mentalidade: de "funções agindo sobre dados" para "dados com comportamentos próprios".
  - **Classe**: O "molde" ou "planta" que define a estrutura e o comportamento.
  - **Objeto (Instância)**: O "biscoito" ou "casa construída" a partir do molde. Uma entidade concreta criada a partir da classe.

- **[10.2 O MÉTODO CONSTRUTOR (`__INIT__`) E O `SELF`](https://docs.python.org/pt-br/3/tutorial/classes.html#class-objects)**: 
  - [`__init__`](https://docs.python.org/pt-br/3/reference/datamodel.html#object.__init__): O método especial que é executado automaticamente quando um objeto é criado. Serve para inicializar os atributos.
  - `self`: Uma referência ao próprio objeto sendo criado. Permite que cada objeto tenha seus próprios atributos independentes (uma analogia excelente para o professor de matemática: é como o $x$ que representa um elemento genérico do conjunto, que ganha um valor específico quando a função é avaliada).

- **[10.3 ATRIBUTOS DE INSTÂNCIA](https://docs.python.org/pt-br/3/tutorial/classes.html#class-and-instance-variables)**: 
  - Dados que pertencem a cada objeto individualmente. São definidos dentro do `__init__` usando `self.atributo = valor`.
  - Cada objeto tem sua própria cópia dos atributos, isolada dos demais.

- **[10.4 MÉTODOS DE INSTÂNCIA](https://docs.python.org/pt-br/3/tutorial/classes.html#method-objects)**: 
  - Funções que pertencem à classe e podem acessar/modificar os atributos do objeto.
  - O primeiro parâmetro de qualquer método de instância é sempre `self`.
  - Permitem que o objeto "faça coisas" com seus próprios dados, encapsulando a lógica interna.
