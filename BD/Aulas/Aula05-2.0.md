# 2. CONCEITOS FUNDAMENTAIS

### 2.1 Mini-Mundo

O **mini-mundo** é um recorte da realidade que queremos representar no sistema. Não precisamos modelar o mundo todo, apenas o que interessa ao negócio.

```mermaid
flowchart LR
    A["🌍 MUNDO REAL<br>(infinitas informações)"] -->|Recorte| B["📦 MINI-MUNDO<br>(a livraria)"]
    B -->|Abstração| C["📋 MODELO CONCEITUAL<br>(o que importa guardar?)"]
    C -->|Refinamento| D["🗂️ MODELO LÓGICO"]
    D -->|Implementação| E["💾 BANCO DE DADOS REAL"]

    style A fill:#fff3e0,stroke:#ef6c00
    style B fill:#e3f2fd,stroke:#1565c0
    style C fill:#c8e6c9,stroke:#2e7d32
    style D fill:#b3e5fc,stroke:#0277bd
    style E fill:#d1c4e9,stroke:#4527a0
```
**Exemplo:** Em um sistema escolar, nosso mini-mundo inclui alunos, professores, disciplinas e notas. Não inclui o clima, o preço do pão na padaria ou o trânsito da cidade.

---

### 2.2 Abstração

**Abstração** é o processo de ignorar detalhes irrelevantes e focar nas características essenciais dos objetos.

> 💡 **Pense assim:** Um mapa de metrô não mostra cada árvore ou prédio da cidade. Ele abstrai a realidade para mostrar apenas estações e linhas. O modelo de dados faz o mesmo!

```mermaid
flowchart TD
    A["🏙️ Cidade Real<br>(Ruas, prédios, árvores, pessoas)"] -->|Abstração| B["🗺️ Mapa de Metrô<br>(Apenas estações e conexões)"]
    
    style A fill:#ffebee,stroke:#c62828
    style B fill:#e8f5e9,stroke:#2e7d32
```

---

### 2.3 Os Três Níveis de Modelagem

| Nível                       | Pergunta que responde                 | Quem entende            | Linguagem               |
| --------------------------- | ------------------------------------- | ----------------------- | ----------------------- |
| **Conceitual** (alto nível) | *"O QUE o sistema guarda?"*           | Cliente, analista, você | Diagramas, português    |
| **Lógico** (intermediário)  | *"COMO os dados estão estruturados?"* | Analista, desenvolvedor | Tabelas, chaves, regras |
| **Físico** (baixo nível)    | *"COMO fica no computador?"*          | SGBD, DBA               | **SQL**                 |

**Fluxo:** Conceitual (o QUÊ) → Lógico (o COMO) → Físico (a IMPLEMENTAÇÃO)

```mermaid
flowchart TD
    A[Modelo Conceitual<br/>DER - Diagrama Entidade-Relacionamento] --> B[Modelo Lógico<br/>Tabelas, Chaves PK e FK]
    B --> C[Modelo Físico<br/>SQL - Implementação no SGBD]
    
    style A fill:#e1f5fe
    style B fill:#fff9c4
    style C fill:#c8e6c9
```

> 📌 O **modelo conceitual** é de alto nível — próximo da linguagem humana. O **modelo físico** é de baixo nível — próximo da linguagem da máquina, escrito em **SQL**. Entre eles, quem gerencia tudo é o **SGBD** (Sistema Gerenciador de Banco de Dados), como MySQL, PostgreSQL e Oracle.

---

### 2.4 MER e DER — QUAL A DIFERENÇA?

| Sigla   | Nome                             | O que é                                                    |
| ------- | -------------------------------- | ---------------------------------------------------------- |
| **MER** | Modelo Entidade-Relacionamento   | O **modelo** — conjunto de conceitos e regras              |
| **DER** | Diagrama Entidade-Relacionamento | O **desenho** — representação gráfica do MER  |

> 🎓 **Analogia**: MER é o "projeto" e DER é o "desenho do projeto no papel". Na prática usamos os termos de forma próxima, mas em prova essa diferença cai!

---

### 2.5 OS PILARES DO MER: ENTIDADE, ATRIBUTO E RELACIONAMENTO

Para construir o MER, precisamos entender seus três componentes fundamentais. Pense neles como as partes de uma frase: **Substantivo, Adjetivo e Verbo**.

#### 1. Entidade (O Substantivo)
É qualquer objeto, pessoa, lugar ou conceito do mini-mundo sobre o qual queremos guardar dados. No DER (notação Chen), é representada por um **retângulo**.
*Exemplo:* `ALUNO`, `LIVRO`, `CLIENTE`.

#### 2. Atributo (O Adjetivo/Característica)
É uma propriedade ou característica de uma entidade (ou de um relacionamento). Na notação Chen, é representado por um **oval**.
*Exemplo:* O aluno tem `Nome`, `CPF`, `Data_Nascimento`.

#### 3. Relacionamento (O Verbo)
É uma associação lógica ou ligação entre duas ou mais entidades. Na notação Chen, é representado por um **losango**.
*Exemplo:* Um ALUNO *MATRICULA-SE* em uma DISCIPLINA.

```mermaid
flowchart TD
    subgraph "Conceitos Básicos (Notação Chen)"
        E1[ENTIDADE 1<br/>Ex: ALUNO]
        E2[ENTIDADE 2<br/>Ex: DISCIPLINA]
        
        R{RELACIONAMENTO<br/>Ex: CURSA}
        
        A1((Atributo<br/>Ex: Nome))
        A2((Atributo<br/>Ex: Código))
    end

    E1 --- A1
    E2 --- A2
    E1 --> R
    E2 --> R

    style E1 fill:#bbdefb,stroke:#1565c0
    style E2 fill:#bbdefb,stroke:#1565c0
    style R fill:#c8e6c9,stroke:#2e7d32
    style A1 fill:#fff3e0,stroke:#ef6c00
    style A2 fill:#fff3e0,stroke:#ef6c00
```

---

### 2.6 CHAVES E CARDINALIDADE (O CORAÇÃO DO MER)

Saber quem são as entidades não basta. Precisamos definir **como elas se identificam** e **como elas se conectam**.

#### 1. Chave Primária (PK - Primary Key)
É o atributo (ou conjunto de atributos) que identifica uma instância da entidade de forma **única e inequívoca**. 
*Exemplo:* O `CPF` no Cliente ou o `ID_LIVRO` no Livro. Na notação Chen, sublinhamos o atributo.

#### 2. Cardinalidade
Define a **quantidade mínima e máxima** de ocorrências de uma entidade que podem (ou devem) se associar a uma ocorrência da outra entidade. É a regra de negócio pura!

*   **1:1 (Um para Um):** Uma instância de A se associa a no máximo uma de B, e vice-versa.
*   **1:N (Um para Muitos):** Uma instância de A se associa a muitas de B, mas uma de B se associa a no máximo uma de A. *(O mais comum!)*
*   **N:M (Muitos para Muitos):** Uma instância de A se associa a muitas de B, e vice-versa.

```mermaid
erDiagram
    %% Exemplo 1:1 (Um CPF para um Passaporte)
    PESSOA ||--|| PASSAPORTE : "possui"
    
    %% Exemplo 1:N (Um departamento tem vários funcionários)
    DEPARTAMENTO ||--|{ FUNCIONARIO : "emprega"
    
    %% Exemplo N:M (Alunos cursam várias disciplinas, disciplinas têm vários alunos)
    ALUNO }|--|{ DISCIPLINA : "cursa"
```
> 💡 **Dica de Ouro:** O diagrama acima usa a notação **Pé de Galinha** (padrão do Mermaid e do mercado). Os símbolos `||` significam "um", `|{` ou `}|` significam "muitos". O lado com `||` é o "1", o lado com `{` ou `}` é o "N".

---

### 2.7 NOTAÇÕES DE DIAGRAMAS ER 🎨

O mesmo modelo pode ser **desenhado** de formas diferentes — o que muda é a **notação**, nunca os conceitos:

| Notação                         | Entidade               | Relacionamento  | Cardinalidade                | Onde é usada                            |
| ------------------------------- | ---------------------- | --------------- | ---------------------------- | --------------------------------------- |
| **Chen**                        | Retângulo ▢            | Losango ◊       | Números nas linhas (1, N)    | Academia, concursos, BrModelo           |
| **Pé de Galinha (Crow's Foot)** | Retângulo              | Sem losango     | Símbolos nas pontas (‖, o{)  | Mercado de trabalho, Mermaid, Workbench |
| **UML (diagrama de classes)**   | Retângulo com divisões | Linha com setas | Multiplicidades (1..*, 0..*) | Desenvolvimento de software OO          |

**Os símbolos da notação de Chen que usaremos:**

| Símbolo | Nome               | Função                                                           |
| :-----: | ------------------ | ---------------------------------------------------------------- |
|    ▢    | Retângulo          | Entidade                                                         |
|    ◊    | Losango            | Relacionamento                                                   |
|    ↝    | Linhas             | Ligam entidades aos relacionamentos                              |
|   𐤏    | Oval               | Atributo                                                         |
|    △    | Triângulo          | Atributo multivalorado **ou** generalização (ver Unidades 3 e 8) |
|    ●    | Círculo preenchido | Chave primária                                                   |

> 💡 **Dica do Professor**: nesta apostila usamos as duas principais! Os diagramas de fluxo seguem a lógica de **Chen** (boa para provas) e os `erDiagram` do Mermaid seguem o **Pé de Galinha** (boa para o mercado). Os conceitos são os mesmos — aprenda a "traduzir" entre elas!
