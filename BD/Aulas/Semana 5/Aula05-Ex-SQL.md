# Criação da tabela Aluno baseada no modelo conceitual

```sql
CREATE TABLE Aluno (
    -- Atributo chave primária, identificador único do aluno
    matricula INT PRIMARY KEY, 
    -- Atributo descritivo, obrigatório (NOT NULL)
    nome VARCHAR(100) NOT NULL, 
    -- Atributo de data, armazenando o nascimento
    data_nascimento DATE 
);
```
