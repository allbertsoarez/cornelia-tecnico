# HERANÇA
Reutilizando código de uma classe pai para uma classe filha.

```text
// Classe Pai (Superclasse)
CLASSE Animal
    ATRIBUTO nome
    ATRIBUTO idade
    
    METODO comer()
        IMPRIMIR nome + " está comendo."
    FIM METODO
FIM CLASSE

// Classe Filha (Subclasse) - Herda de Animal
CLASSE Cachorro HERDA DE Animal
    ATRIBUTO raca // Atributo exclusivo do Cachorro
    
    METODO latir() // Método exclusivo do Cachorro
        IMPRIMIR nome + " está latindo: Au au!"
    FIM METODO
FIM CLASSE

// Uso:
meuCao = NOVO Cachorro()
meuCao.nome = "Rex"      // Herdado de Animal
meuCao.raca = "Pastor"   // Exclusivo de Cachorro
meuCao.comer()           // Método herdado
meuCao.latir()           // Método próprio
```
