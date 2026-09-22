## 6. Domínio e Regras de Integridade

### 6.1 Domínio de Atributos

O **domínio** é o conjunto de todos os valores válidos que um atributo pode assumir.

```mermaid
erDiagram
    ALUNO {
        string sexo "Domínio: 'M', 'F', 'N'"
        int idade "Domínio: números inteiros >= 0"
        float nota "Domínio: números reais entre 0 e 10"
    }
```

>  **Exemplo:** O domínio do atributo `sexo` pode ser restrito a {'M', 'F', 'N'}. Não podemos armazenar "ABC" nesse campo!

### 6.2 Regras de Integridade

#### Integridade de Entidade
- A **Chave Primária** nunca pode ser nula (vazia)
- A **Chave Primária** deve ser única

```mermaid
erDiagram
    ALUNO {
        int matricula PK "NUNCA pode ser NULL e deve ser único"
        string nome
    }
```

#### Integridade Referencial
- Uma **Chave Estrangeira** só pode conter valores que já existem na Chave Primária da tabela de origem
- Ou ser nula (se a regra de negócio permitir)

```mermaid
erDiagram
    CLIENTE ||--|{ PEDIDO : "faz"
    
    CLIENTE {
        int id PK
        string nome
    }
    
    PEDIDO {
        int numero PK
        int cliente_id FK "Só pode conter IDs que existem em CLIENTE"
    }
```

> 💡 **Analogia:** As regras de integridade são os "fiscais" do banco de dados. Elas impedem que o sistema aceite um pedido de compra de um cliente que não existe!
