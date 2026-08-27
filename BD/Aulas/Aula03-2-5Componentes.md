# CINCO COMPONENTES FUNDAMENTAIS

Um excelente exemplo prático de um Sistema de Banco de Dados (SBD) no mundo real é um Sistema Bancário de Contas e Transferências. Para que este SBD funcione como um ecossistema completo e integrado, ele precisa da interação obrigatória de seus 5 componentes fundamentais

## 1. DADOS

Os Dados: Consistem nos saldos das contas correntes, números de agências, senhas criptografadas, CPFs dos clientes e o histórico completo de cada transação realizada.

---
## 2. HARDWARE

O Hardware: Representa a infraestrutura física, como os servidores dedicados do banco (ou servidores em nuvem), os discos de armazenamento de alta velocidade (como SSDs) onde os bits dos dados estão gravados e os equipamentos de rede que conectam as agências e os aplicativos móveis.

---
## 3. SOFTWARE  
  
  O Software (SGBD): É o motor central, como o Oracle ou o PostgreSQL 5. Ele é o "bibliotecário chefe" encarregado de ler e gravar os dados fisicamente no disco rígido, garantindo que o dinheiro saia de uma conta e entre na outra com total consistência 4, 6.

---
## 4. PESSOAS

- **Os usuários finais** (clientes que usam o aplicativo no celular para fazer um Pix ou consultar o saldo).
- **Os desenvolvedores** que criam e atualizam o aplicativo do banco.
- **Os Administradores de Banco de Dados (DBAs)**, que monitoram e otimizam a performance do sistema para garantir que ele não fique lento.

---
## 5. PROCEDIMENTOS

Os Procedimentos: São as regras operacionais rigorosas, como a execução diária de backups automáticos na madrugada, as políticas de segurança de dados para atender à LGPD e as regras de transação automática (rollback) caso a energia do servidor caia no exato momento de uma transferência.

---
**IMPORTANTE**

Se qualquer um desses cinco componentes falhar — por exemplo, se o hardware queimar, se os procedimentos de backup não funcionarem ou se o SGBD apresentar uma falha de concorrência —, o sistema financeiro inteiro colapsará. É por isso que o SBD é considerado a visão macro e a infraestrutura completa da informação em uma organização.
