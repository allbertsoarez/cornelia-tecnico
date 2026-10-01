### 14. Projeto Final Integrador - Agenda Gráfica na Nuvem
Neste módulo, consolidamos todo o conhecimento adquirido (POO, Persistência, Tratamento de Erros e Interfaces) em um projeto de portfólio completo, executado inteiramente no Google Colab.

- **14.1 Integração com o Google Drive**: 
  - Uso do módulo `google.colab.drive` para montar o disco virtual do aluno.
  - Salvamento de arquivos JSON em pastas permanentes, garantindo que os dados não sejam perdidos ao reiniciar o notebook.

- **14.2 Interfaces Gráficas no Colab (`ipywidgets`)**: 
  - Criação de componentes visuais: `Text` (caixas de entrada), `Button` (botões de ação) e `Output` (áreas de exibição).
  - Organização do layout usando `VBox` (caixas verticais) e `HBox` (caixas horizontais).
  - Associação de eventos (cliques de botão) a funções Python.

- **14.3 Arquitetura do Projeto (CRUD com POO)**: 
  - Modelagem do problema: Criação da classe `Contato` (dados) e da classe `Agenda` (lógica de negócios e persistência).
  - Implementação das operações CRUD: **C**riar, **R**ead (Ler/Listar), **U**pdate (não implementado neste desafio, mas sugerido), **D**eletar.
  - Encapsulamento do tratamento de erros e da leitura/escrita do JSON dentro dos métodos da classe.
