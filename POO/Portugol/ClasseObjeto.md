# Classe e Objeto (A Base)
Antes dos pilares, precisamos entender como criar o molde e a instância.

```text
// Definindo a Classe (o molde)
CLASSE Carro
    ATRIBUTO cor
    ATRIBUTO modelo
    
    METODO ligar()
        IMPRIMIR "O carro está ligado!"
    FIM METODO
FIM CLASSE

// Criando o Objeto (a instância concreta)
meuCarro = NOVO Carro()
meuCarro.cor = "Azul"
meuCarro.modelo = "Fusca"
meuCarro.ligar() // Saída: O carro está ligado!
```
