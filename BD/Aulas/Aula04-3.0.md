## 3. Entidades e Atributos

### 3.1 Entidade ▢

A **entidade** representa um conjunto de objetos do mundo real (pessoas, coisas, conceitos) sobre os quais queremos armazenar informações.

**Características:**
- Representada por um **retângulo** no DER
- Nomeada no **singular** e em **letras maiúsculas**
- Pode ser **Forte** (existência independente) ou **Fraca** (depende de outra entidade)

```mermaid
erDiagram
    ALUNO
    PROFESSOR
    DISCIPLINA
```

> 💡 **Dica:** Pense em entidade como um **conjunto** na matemática. "ALUNO" é o conjunto de todos os alunos da escola.

### 3.2 Atributos 𐤏

Os **atributos** são as características que descrevem uma entidade. No banco de dados, eles se tornam as **colunas** das tabelas.

```mermaid
erDiagram
    ALUNO {
        int matricula
        string nome
        date data_nascimento
        string cpf
        string email
    }
```

### 3.3 Tipos de Atributos

#### Atributo Simples
Não pode ser dividido em partes menores.

```mermaid
erDiagram
    ALUNO {
        string cpf "Simples - não pode ser dividido"
    }
```

#### Atributo Composto
Pode ser dividido em partes menores.

```mermaid
erDiagram
    ALUNO {
        string endereco_rua
        string endereco_cidade
        string endereco_estado
        string endereco_cep
    }
```

#### Atributo Multivalorado △
Pode ter vários valores para uma mesma entidade.

```mermaid
erDiagram
    ALUNO {
        int matricula
        string nome
        string telefones[] "Multivalorado - pode ter vários"
        string emails[] "Multivalorado - pode ter vários"
    }
```

> 💡 **Exemplo prático:** Uma pessoa pode ter telefone residencial, celular e comercial. Por isso, "telefone" é multivalorado.

#### Atributo Derivado
Seu valor é calculado a partir de outro atributo.

```mermaid
erDiagram
    ALUNO {
        date data_nascimento "Armazenado"
        int idade "Derivado - calculado a partir da data de nascimento"
    }
```

### 3.4 Chave Primária ●

A **chave primária** (Primary Key - PK) é o atributo que identifica **exclusivamente** cada instância da entidade.

```mermaid
erDiagram
    ALUNO {
        int matricula PK "Chave Primária - única para cada aluno"
        string nome
        string cpf
    }
    
    PRODUTO {
        int codigo PK
        string nome
        float preco
    }
```

> 💡 **Regra de Ouro:** Toda entidade forte PRECISA de uma chave primária. Ela é como o CPF da entidade - não pode ser nula e deve ser única!

---

## 4. Relacionamentos e Cardinalidades

### 4.1 O Relacionamento ◊

O **relacionamento** é a associação significativa entre duas ou mais entidades. É o "verbo" que conecta os "sujeitos" do nosso modelo.

```mermaid
erDiagram
    ALUNO ||--o{ MATRICULA : "realiza"
    CURSO ||--o{ MATRICULA : "oferece"
```

> 💡 **Dica:** Entidade = SUBSTANTIVO (Aluno, Curso). Relacionamento = VERBO (Matricula-se, Cursa).

### 4.2 Cardinalidade ()

A **cardinalidade** define as regras de negócio - quantas instâncias de uma entidade podem se relacionar com quantas instâncias de outra entidade.

#### Cardinalidade 1:1 (Um para Um)

```mermaid
erDiagram
    DIRETOR ||--|| DEPARTAMENTO : "gerencia"
```

**Exemplo:** Um diretor gerencia apenas 1 departamento, e um departamento tem apenas 1 diretor.

#### Cardinalidade 1:N (Um para Muitos)

```mermaid
erDiagram
    EDITORA ||--|{ LIVRO : "publica"
```

**Exemplo:** Uma editora publica muitos livros, mas um livro pertence a uma única editora.

#### Cardinalidade N:M (Muitos para Muitos)

```mermaid
erDiagram
    ALUNO }|--|{ DISCIPLINA : "cursa"
```

**Exemplo:** Um aluno cursa várias disciplinas, e uma disciplina tem vários alunos.

> ️ **Atenção:** No modelo lógico/físico, relacionamentos N:M precisam de uma **entidade associativa**!

### 4.3 Entidade Associativa

Quando temos um relacionamento N:M, criamos uma entidade associativa para transformá-lo em dois relacionamentos 1:N.

```mermaid
erDiagram
    ALUNO ||--o{ MATRICULA : "realiza"
    DISCIPLINA ||--o{ MATRICULA : "é matriculada em"
    
    MATRICULA {
        int id PK
        date data_matricula
        float nota
    }
```

**Explicação:** A entidade `MATRICULA` associa `ALUNO` e `DISCIPLINA`, e pode ter atributos próprios como `data_matricula` e `nota`.

---

## 5. Chaves: Primária e Estrangeira

### 5.1 Chave Primária (PK) ●

Já vimos: é o identificador único da entidade.

```mermaid
erDiagram
    CLIENTE {
        int id PK
        string nome
        string cpf
    }
```

### 5.2 Chave Estrangeira (FK)

A **chave estrangeira** (Foreign Key) é o atributo que faz referência à chave primária de outra entidade. É o "elo de ligação" que materializa o relacionamento.

```mermaid
erDiagram
    CLIENTE {
        int id PK
        string nome
    }
    
    PEDIDO {
        int numero PK
        date data_pedido
        int cliente_id FK "Chave Estrangeira - referencia CLIENTE"
    }
    
    CLIENTE ||--|{ PEDIDO : "faz"
```

> 💡 **Analogia:** Se a Chave Primária é a identidade da entidade, a Chave Estrangeira é o "endereço" que nos diz onde encontrar a entidade relacionada.

### 5.3 Entidades Fracas e Chaves

Entidades fracas recebem a chave primária da entidade forte como parte de sua própria chave.

```mermaid
erDiagram
    EDITORA ||--|{ LIVRO : "publica"
    
    EDITORA {
        int cod_editora PK
        string nome
    }
    
    LIVRO {
        int cod_livro
        int cod_editora FK "Parte da chave + cod_livro formam a chave"
        string titulo
    }
```

---

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

---

## 7. Exemplo Prático: Transformando MER em Modelo Lógico

### Cenário: Sistema de Biblioteca

Vamos criar um modelo conceitual e transformá-lo em modelo lógico (tabelas).

### Passo 1: Modelo Conceitual (MER)

```mermaid
erDiagram
    AUTOR ||--|{ LIVRO : "escreve"
    EDITORA ||--|{ LIVRO : "publica"
    ALUNO ||--|{ EMPRESTIMO : "realiza"
    LIVRO ||--|{ EMPRESTIMO : "é emprestado em"
    
    AUTOR {
        int cod_autor PK
        string nome
        string nacionalidade
    }
    
    EDITORA {
        int cod_editora PK
        string nome
        string endereco
    }
    
    LIVRO {
        int cod_livro PK
        string titulo
        int ano_publicacao
        int cod_autor FK
        int cod_editora FK
    }
    
    ALUNO {
        int matricula PK
        string nome
        string telefone[]
        string email
    }
    
    EMPRESTIMO {
        int numero PK
        date data_retirada
        date data_devolucao
        int matricula_aluno FK
        int cod_livro FK
    }
```

### Passo 2: Transformação em Modelo Lógico (Tabelas)

Agora vamos transformar cada entidade em uma **tabela**, seguindo estas regras:

#### Regras de Transformação:

1. **Cada entidade vira uma tabela**
2. **Cada atributo vira uma coluna**
3. **A chave primária (PK) é mantida**
4. **Os relacionamentos 1:N viram chaves estrangeiras (FK)**
5. **Os relacionamentos N:M viram tabelas associativas**

### Passo 3: Estrutura das Tabelas

#### Tabela: AUTOR

| Coluna | Tipo | Restrição |
|--------|------|-----------|
| cod_autor | INT | PRIMARY KEY |
| nome | VARCHAR(100) | NOT NULL |
| nacionalidade | VARCHAR(50) | - |

#### Tabela: EDITORA

| Coluna | Tipo | Restrição |
|--------|------|-----------|
| cod_editora | INT | PRIMARY KEY |
| nome | VARCHAR(100) | NOT NULL |
| endereco | VARCHAR(200) | - |

#### Tabela: LIVRO

| Coluna | Tipo | Restrição |
|--------|------|-----------|
| cod_livro | INT | PRIMARY KEY |
| titulo | VARCHAR(150) | NOT NULL |
| ano_publicacao | INT | - |
| cod_autor | INT | FOREIGN KEY → AUTOR(cod_autor) |
| cod_editora | INT | FOREIGN KEY → EDITORA(cod_editora) |

**Explicação:** 
- `cod_autor` e `cod_editora` são **chaves estrangeiras** que referenciam as tabelas AUTOR e EDITORA
- Isso representa os relacionamentos 1:N (um autor escreve muitos livros, uma editora publica muitos livros)

#### Tabela: ALUNO

| Coluna | Tipo | Restrição |
|--------|------|-----------|
| matricula | INT | PRIMARY KEY |
| nome | VARCHAR(100) | NOT NULL |
| email | VARCHAR(100) | - |

**Nota:** O atributo multivalorado `telefone[]` precisaria de uma tabela separada (TELEFONE_ALUNO) no modelo lógico completo.

#### Tabela: EMPRESTIMO

| Coluna | Tipo | Restrição |
|--------|------|-----------|
| numero | INT | PRIMARY KEY |
| data_retirada | DATE | NOT NULL |
| data_devolucao | DATE | - |
| matricula_aluno | INT | FOREIGN KEY → ALUNO(matricula) |
| cod_livro | INT | FOREIGN KEY → LIVRO(cod_livro) |

**Explicação:**
- `matricula_aluno` referencia o aluno que fez o empréstimo
- `cod_livro` referencia o livro emprestado
- Isso representa o relacionamento entre ALUNO e LIVRO

### Passo 4: Visualização do Modelo Lógico

```mermaid
erDiagram
    AUTOR {
        int cod_autor PK
        string nome
        string nacionalidade
    }
    
    EDITORA {
        int cod_editora PK
        string nome
        string endereco
    }
    
    LIVRO {
        int cod_livro PK
        string titulo
        int ano_publicacao
        int cod_autor FK
        int cod_editora FK
    }
    
    ALUNO {
        int matricula PK
        string nome
        string email
    }
    
    EMPRESTIMO {
        int numero PK
        date data_retirada
        date data_devolucao
        int matricula_aluno FK
        int cod_livro FK
    }
    
    AUTOR ||--|{ LIVRO : "1:N"
    EDITORA ||--|{ LIVRO : "1:N"
    ALUNO ||--|{ EMPRESTIMO : "1:N"
    LIVRO ||--|{ EMPRESTIMO : "1:N"
```

### Resumo da Transformação

| Elemento do MER            | Elemento no Modelo Lógico         |
| -------------------------- | --------------------------------- |
| Entidade                   | Tabela                            |
| Atributo                   | Coluna                            |
| Chave Primária (●)         | PRIMARY KEY                       |
| Relacionamento 1:N         | FOREIGN KEY na tabela do lado "N" |
| Relacionamento N:M         | Tabela associativa com duas FKs   |
| Atributo Multivalorado (△) | Tabela separada                   |
