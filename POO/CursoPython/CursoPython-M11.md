### 11. POO Avançada e Herança
Neste módulo, elevamos a Programação Orientada a Objetos a um nível profissional, aprendendo a reutilizar código, proteger dados e criar sistemas flexíveis.

- **11.1 Herança**: 
  - O conceito de criar uma **Classe Filha (Derivada)** a partir de uma **Classe Pai (Base)**.
  - A classe filha herda automaticamente todos os atributos e métodos da classe pai, permitindo reutilização de código.
  - O uso da função `super()` para chamar o construtor da classe pai e inicializar atributos herdados.

- **11.2 Polimorfismo (Sobrescrita de Métodos)**: 
  - A capacidade de uma classe filha **redefinir (sobrescrever)** um método que já existe na classe pai.
  - Permite que objetos de classes diferentes respondam ao "mesmo comando" de formas específicas e especializadas.

- **11.3 Encapsulamento e Proteção de Dados**: 
  - A convenção do underline simples (`_atributo`) para indicar que um atributo é "privado" (uso interno).
  - O "Name Mangling" do underline duplo (`__atributo`) para proteger atributos críticos de acessos acidentais.
  - **Getters e Setters Elegantes**: O uso do decorador `@property` para criar métodos que se comportam como atributos, permitindo validação de dados ao ler ou modificar um valor.

- **11.4 Métodos Mágicos (Dunder Methods)**: 
  - Métodos especiais delimitados por duplo underline (ex: `__str__`, `__repr__`).
  - O método `__str__(self)`: Define como o objeto será representado em texto quando usamos a função `print()` nele, substituindo aquela mensagem feia de "memória do objeto".
