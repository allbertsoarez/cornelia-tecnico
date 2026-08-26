# FASES DE UM PROJETO DE BANCO DE DADOS 


O erro clássico do iniciante é achar que projetar um banco de dados é simplesmente abrir o MySQL ou o PostgreSQL e começar a criar tabelas. Fazer isso é como querer construir um prédio de dez andares comprando tijolos e cimento sem ter a planta do arquiteto ou o cálculo estrutural do engenheiro. O resultado? A estrutura colapsa.

### 1. LEVANTAMENTO E ANÁLISE DE REQUISITOS

Tudo começa aqui. Antes de falar de tabelas, chaves ou índices, você precisa entender o problema do negócio. O que o sistema vai armazenar? Quem vai usar? Quais são as regras da empresa? 
Nesta fase, o projetista se reúne com os usuários, analisa documentos e mapeia os processos. O produto final desta etapa é o **Dicionário de Dados** e um documento de requisitos. 
*O que é fundamental aqui:* Se você pular ou fizer um levantamento de requisitos mal feito, o banco de dados estará fadado ao fracasso. Não adianta ter um código perfeito se ele não resolve a necessidade real do cliente.

### 2. PROJETO CONCEITUAL

Com os requisitos em mãos, vamos para a prancheta. O projeto conceitual é a criação de um modelo de alto nível que representa as informações e as regras do negócio, **independentemente de qualquer Sistema Gerenciador de Banco de Dados (SGBD)**. 
Aqui, utilizamos a ferramenta mais clássica e didática da área: o **Modelo Entidade-Relacionamento (MER)**, proposto por Peter Chen. Nós desenhamos as Entidades (os "substantivos" do negócio, como ALUNO, CURSO), seus Atributos (as características) e os Relacionamentos (como eles interagem). 

*O que é fundamental aqui:* Entender que o modelo conceitual é a "ponte" entre o mundo real (o negócio) e o mundo computacional. Ele deve ser compreensível tanto pelo técnico quanto pelo cliente.

### 3. PROJETO LÓGICO

Agora a coisa fica mais técnica. O projeto lógico pega o nosso diagrama conceitual e o traduz para um modelo de dados específico, que no nosso curso e no mercado é majoritariamente o **Modelo Relacional**, idealizado por Edgar F. Codd.

Nesta fase, transformamos entidades e relacionamentos em **Tabelas**. Definimos as Chaves Primárias (que identificam unicamente cada registro) e as Chaves Estrangeiras (que ligam as tabelas). 

*O que é fundamental aqui:* É no projeto lógico que aplicamos a **Normalização**. Nós passamos as tabelas pelas Formas Normais (1FN, 2FN, 3FN) para eliminar redundâncias e evitar anomalias de inserção, atualização e exclusão. Um projeto lógico bem normalizado é a garantia de um banco de dados íntegro e consistente.

### 4. PROJETO FÍSICO

Chegamos à fase onde escolhemos a "ferramenta". O projeto físico é a implementação do modelo lógico em um SGBD específico (como Oracle, SQL Server, PostgreSQL ou MySQL). 
Aqui, o projetista toma decisões de desempenho e armazenamento:

- Quais colunas terão índices para acelerar as buscas? 
- Como os dados serão fisicamente alocados em disco? 
- Quais serão as regras de segurança?
- Usuários e permissões de acesso?

*O que é fundamental aqui:* Entender que o projeto físico é dependente do SGBD. O que funciona para otimizar o MySQL pode não ser a melhor prática no PostgreSQL. O foco aqui é **performance e otimização**.

### 5. IMPLEMENTAÇÃO, TESTES E MANUTENÇÃO

Por fim, saímos do papel e vamos para o código. Nesta fase, utilizamos a linguagem SQL para criar a estrutura (comandos DDL, como `CREATE TABLE`), inserir os dados iniciais (DML) e criar as visões e procedimentos armazenados.

Após a implementação, realizamos testes rigorosos de carga e validação com os usuários. E não se enganem: o ciclo não termina aqui. O banco de dados entra em fase de **Manutenção e Evolução**, onde novos requisitos surgirão, exigindo que o banco seja reajustado, voltando, muitas vezes, para a fase de requisitos.

### CONCLUSÃO

Turma, para encerrar a aula de hoje, quero que levem a seguinte mensagem: um projeto de banco de dados não é linear, é iterativo. Mas a ordem das fases — Requisitos, Conceitual, Lógico, Físico e Implementação — deve ser rigorosamente respeitada. 

O que separa um técnico medíocre de um excelente profissional é a disciplina de não pular etapas. O modelo conceitual garante que você entendeu o negócio; o modelo lógico garante que seus dados não terão redundâncias; e o modelo físico garante que o sistema será rápido e seguro. 

Estudem os conceitos de Modelagem Entidade Relacionamento e Normalização, pois eles são o coração das fases conceitual e lógica.
