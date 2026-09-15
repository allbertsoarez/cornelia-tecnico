# 📘MODELAGEM DE DADOS - DO CONCEITUAL AO LÓGICO

## 1. FUNDAMENTOS DA MODELAGEM DE DADOS

Imagine construir um prédio sem planta arquitetônica: o encanador passa os canos onde depois virá uma parede, e refazer tudo custa 10x mais caro. Com bancos de dados é igual: **modelar primeiro economiza meses de retrabalho**. O erro mais comum do iniciante é abrir o SGBD e começar a "criar tabela". O profissional desenha primeiro, implementa depois.

### 1.2 MINI MUNDO E ABSTRAÇÃO

| Conceito | Definição | Exemplo |
|----------|-----------|---------|
| **Mini-mundo** (Universo de Discurso) | Recorte do mundo real que o sistema vai representar. | A livraria (não a cidade inteira!). |
| **Abstração** | Escolher/isolar apenas os aspectos relevantes, ignorando detalhes inúteis. | Guardamos o CPF do cliente, mas não a cor dos olhos dele. |

> 💡 **Conexão Matemática:** Assim como um mapa de metrô abstrai a cidade (ignorando árvores e prédios) para mostrar apenas estações (nós) e linhas (arestas), o modelo de dados abstrai o negócio para mostrar apenas as entidades e seus relacionamentos.

### 1.3 OS TRÊS NÍVEIS DO MODELO

```mermaid
flowchart LR
    A["🌍 MUNDO REAL"] -->|Recorte| B["📦 MINI-MUNDO"]
    B -->|Abstração| C["📋 MODELO CONCEITUAL (O QUÊ?)"]
    C -->|Refinamento| D["🗂️ MODELO LÓGICO (COMO?)"]
    D -->|Implementação| E["💾 MODELO FÍSICO / SQL (ONDE?)"]
    
    style A fill:#fff3e0,stroke:#ef6c00
    style C fill:#c8e6c9,stroke:#2e7d32
    style D fill:#b3e5fc,stroke:#0277bd
    style E fill:#d1c4e9,stroke:#4527a0
```

- **Conceitual:** Próximo da linguagem humana (Diagramas).
- **Lógico:** Estruturas de tabelas, chaves e regras (Independente de SGBD).
- **Físico:** Implementação real no SGBD (MySQL, PostgreSQL) via linguagem SQL.

---

### 1.4 MER vs. DER e NOTAÇÕES

| Sigla   | Nome                             | O que é                                        |
| ------- | -------------------------------- | ---------------------------------------------- |
| **MER** | Modelo Entidade-Relacionamento   | O **modelo** (conjunto de conceitos e regras). |
| **DER** | Diagrama Entidade-Relacionamento | O **desenho** (representação gráfica do MER).  |

**Notações Gráficas:** Os conceitos são os mesmos, mas o desenho muda:

- **Notação de Chen:**
- Usa retângulos (▢),
- losangos (◊) e
- ovais (𐤏).

  Muito usada em concursos e academia.
- **Notação "Pé de Galinha" (Crow's Foot):** Usa retângulos com atributos internos e símbolos nas pontas das linhas (`||`, `o{`). Usada no mercado de trabalho (Mermaid, MySQL Workbench, BrModelo). *Esta apostila utiliza a notação Pé de Galinha nos diagramas Mermaid por ser a padrão de mercado, mas os conceitos de Chen são plenamente aplicáveis.*
