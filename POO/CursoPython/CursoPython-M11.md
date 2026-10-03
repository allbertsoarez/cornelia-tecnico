### 11. [POO AVANÇADA E HERANÇA](https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance)
Neste módulo, elevamos a Programação Orientada a Objetos a um nível profissional, aprendendo a reutilizar código, proteger dados e criar sistemas flexíveis.

- **[11.1 HERANÇA](https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance)**: 
  - O conceito de criar uma **Classe Filha (Derivada)** a partir de uma **Classe Pai (Base)**.
  - A classe filha herda automaticamente todos os atributos e métodos da classe pai, permitindo reutilização de código.
  - O uso da função [`super()`](https://docs.python.org/pt-br/3/library/functions.html#super) para chamar o construtor da classe pai e inicializar atributos herdados de forma elegante.

- **[11.2 POLIMORFISMO (SOBRESCRITA DE MÉTODOS)](https://docs.python.org/pt-br/3/glossary.html#term-polymorphism)**: 
  - A capacidade de uma classe filha **redefinir (sobrescrever)** um método que já existe na classe pai.
  - Permite que objetos de classes diferentes respondam ao "mesmo comando" de formas específicas e especializadas, adaptando o comportamento ao seu contexto.

- **[11.3 ENCAPSULAMENTO E PROTEÇÃO DE DADOS](https://docs.python.org/pt-br/3/tutorial/classes.html#tut-private)**: 
  - A convenção do underline simples (`_atributo`) para indicar que um atributo é "privado" (uso interno da classe).
  - O "Name Mangling" do underline duplo (`__atributo`) para proteger atributos críticos de acessos ou sobrescritas acidentais por subclasses.
  - **Getters e Setters Elegantes**: O uso do decorador [`@property`](https://docs.python.org/pt-br/3/library/functions.html#property) para criar métodos que se comportam como atributos, permitindo validação de dados ao ler ou modificar um valor sem alterar a interface pública da classe.

- **[11.4 MÉTODOS MÁGICOS (DUNDER METHODS)](https://docs.python.org/pt-br/3/reference/datamodel.html#special-method-names)**: 
  - Métodos especiais delimitados por duplo underline (ex: [`__str__`](https://docs.python.org/pt-br/3/reference/datamodel.html#object.__str__), [`__repr__`](https://docs.python.org/pt-br/3/reference/datamodel.html#object.__repr__)).
  - O método `__str__(self)`: Define como o objeto será representado em texto quando usamos a função `print()` nele, substituindo aquela mensagem genérica de "endereço de memória do objeto" (ex: `<__main__.Objeto object at 0x...>`) por algo legível e útil.

---

````mermaid
flowchart TD
    subgraph Heranca ["Herança e Reutilização"]
        A["Classe Pai (Base)"] -->|Herda tudo| B["Classe Filha (Derivada)"]
        B --> C["Uso de super()\nInicializa a parte da Classe Pai"]
    end

    subgraph Polimorfismo ["Polimorfismo e Sobrescrita"]
        D["Mesmo Nome de Método"] --> E["Comportamento Padrão na Classe Pai"]
        D --> F["Comportamento Especializado na Classe Filha"]
    end

    subgraph Encapsulamento ["Encapsulamento e Proteção"]
        G["Atributo Público"] --> H["Acesso livre por qualquer código"]
        I["Atributo Protegido _nome"] --> J["Convenção de uso interno"]
        K["Atributo Privado __nome"] --> L["Name Mangling com proteção forte"]
        M["Decorador @property"] --> N["Getters e Setters elegantes\ncom validação de dados"]
    end

    subgraph Representacao ["Métodos Mágicos ou Dunder"]
        O["Objeto na Memória"] -->|Chamada por print| P["Método __str__"]
        P --> Q["Texto legível e amigável\nao invés de endereço de memória"]
    end



