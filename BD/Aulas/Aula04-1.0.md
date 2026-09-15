# 📘MODELAGEM DE DADOS - DO CONCEITUAL AO LÓGICO

## 1. Introdução à Modelagem de Dados

**🎯 Por que modelar dados?**

Imagine que você precisa construir uma casa. Você começaria a levantar paredes sem uma planta baixa? Provavelmente não! Com bancos de dados é a mesma coisa: **a modelagem é a planta baixa do seu sistema**.

> 💡 **Analogia:** Assim como um arquiteto desenha a casa antes de construí-la, nós desenhamos o banco de dados antes de implementá-lo.


### 2.1 Mini-Mundo (Universo de Discurso)

O **mini-mundo** é um recorte da realidade que queremos representar no sistema. Não precisamos modelar o mundo todo, apenas o que interessa ao negócio.

**Exemplo:** Em um sistema escolar, nosso mini-mundo inclui alunos, professores, disciplinas e notas. Não inclui o clima, o preço do pão na padaria ou o trânsito da cidade.





### 1.2 Os Três Níveis de Modelo

| Nível                       | Pergunta que responde                 | Quem entende            | Linguagem               |
| --------------------------- | ------------------------------------- | ----------------------- | ----------------------- |
| **Conceitual** (alto nível) | *"O QUÊ o sistema guarda?"*           | Cliente, analista       | Diagramas (DER)         |
| **Lógico** (intermediário)  | *"COMO os dados estão estruturados?"* | Analista, desenvolvedor | Tabelas, chaves, regras |
| **Físico** (baixo nível)    | *"COMO fica no computador?"*          | SGBD, DBA               | **SQL**                 |

> 📌 O **SGBD** (Sistema Gerenciador de Banco de Dados) — como MySQL, PostgreSQL e Oracle — é o software que gerencia o banco implementado.

### 1.3 MER × DER — Qual a diferença?

| Sigla   | Nome                             | O que é                                       |
| ------- | -------------------------------- | --------------------------------------------- |
| **MER** | Modelo Entidade-Relacionamento   | O **modelo** — conjunto de conceitos e regras |
| **DER** | Diagrama Entidade-Relacionamento | O **desenho** — representação gráfica do MER  |

> 🎓 **Analogia:** MER é o "projeto"; DER é o "desenho do projeto no papel". Em prova, essa diferença cai!
