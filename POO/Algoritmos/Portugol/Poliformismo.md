# POLIFORMISMO
Diferentes objetos respondendo à mesma mensagem (método) de formas diferentes.

```text
CLASSE Animal
    METODO emitirSom()
        // Implementação genérica ou vazia
    FIM METODO
FIM CLASSE

CLASSE Cachorro HERDA DE Animal
    METODO SOBRESCREVER emitirSom()
        IMPRIMIR "Au au!"
    FIM METODO
FIM CLASSE

CLASSE Gato HERDA DE Animal
    METODO SOBRESCREVER emitirSom()
        IMPRIMIR "Miau!"
    FIM METODO
FIM CLASSE

// Uso do Polimorfismo:
listaDeAnimais = [NOVO Cachorro(), NOVO Gato()]

PARA CADA animal EM listaDeAnimais FAÇA
    // A mesma chamada, mas comportamentos diferentes!
    animal.emitirSom()
FIM PARA

// Saída:
// Au au!
// Miau!
```
