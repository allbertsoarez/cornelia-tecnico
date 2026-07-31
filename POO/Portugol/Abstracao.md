5. Abstração

Focando no **o que** o objeto faz, escondendo o **como** e forçando as classes filhas a implementarem suas próprias versões de métodos abstratos.

```text
// Classe Abstrata: não pode ser instanciada diretamente (não existe um "Veículo" genérico puro)
CLASSE ABSTRATA Veiculo
    ATRIBUTO velocidadeAtual
    
    // Método Abstrato: apenas a assinatura, sem implementação.
    // Obriga as filhas a dizerem COMO elas se movem.
    METODO ABSTRATO mover() 
FIM CLASSE

CLASSE Aviao HERDA DE Veiculo
    METODO SOBRESCREVER mover()
        IMPRIMIR "O avião está decolando e voando pelos ares!"
    FIM METODO
FIM CLASSE

CLASSE Submarino HERDA DE Veiculo
    METODO SOBRESCREVER mover()
        IMPRIMIR "O submarino está mergulhando e navegando submerso!"
    FIM METODO
FIM CLASSE

// Uso:
meuAviao = NOVO Aviao()
meuAviao.mover() // Saída: O avião está decolando e voando pelos ares!

// meuTransporte = NOVO Veiculo() <-- ERRO! Não se pode criar objeto de classe abstrata.
```