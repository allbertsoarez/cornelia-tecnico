# Encapsulamento
Protegendo os dados internos e expondo apenas o necessário através de métodos.

```text
CLASSE ContaBancaria
    // Atributo PRIVADO: não pode ser acessado diretamente de fora
    ATRIBUTO PRIVADO saldo = 0.0 
    
    // Métodos PÚBLICOS: a única forma de interagir com o saldo
    METODO PUBLICO depositar(valor)
        SE valor > 0 ENTAO
            saldo = saldo + valor
            IMPRIMIR "Depósito realizado. Novo saldo: " + saldo
        FIM SE
    FIM METODO
    
    METODO PUBLICO verSaldo()
        IMPRIMIR "Saldo atual: " + saldo
    FIM METODO
FIM CLASSE

// Uso correto:
minhaConta = NOVO ContaBancaria()
minhaConta.depositar(100.0) 

// Uso INCORRETO (o sistema bloquearia, pois 'saldo' é privado):
// minhaConta.saldo = 1000000.0  <-- ERRO! Acesso negado.
```
