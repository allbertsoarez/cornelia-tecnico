## 2. CONCEITOS FUNDAMENTAIS
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

> 📌 O **modelo conceitual** é de alto nível — próximo da linguagem humana. O **modelo físico** é de baixo nível — próximo da linguagem da máquina, escrito em **SQL**. Entre eles, quem gerencia tudo é o **SGBD** (Sistema Gerenciador de Banco de Dados), como MySQL, PostgreSQL e Oracle 【turn0fetch0】.

