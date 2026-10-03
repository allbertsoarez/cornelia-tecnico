### 14. [PROJETO FINAL INTEGRADOR - AGENDA GRÁFICA NA NUVEM](https://colab.research.google.com/notebooks/intro.ipynb)
Neste módulo, consolidamos todo o conhecimento adquirido (POO, Persistência, Tratamento de Erros e Interfaces) em um projeto de portfólio completo, executado inteiramente no Google Colab.

- **[14.1 INTEGRAÇÃO COM O GOOGLE DRIVE](https://colab.research.google.com/notebooks/io.ipynb)**: 
  - Uso do módulo [`google.colab.drive`](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=u2l5q3UeDAgq) para montar o disco virtual do aluno.
  - Salvamento de arquivos JSON em pastas permanentes, garantindo que os dados não sejam perdidos ao reiniciar o notebook.

- **[14.2 INTERFACES GRÁFICAS NO COLAB (`IPYWIDGETS`)](https://ipywidgets.readthedocs.io/en/stable/)**: 
  - Criação de componentes visuais: [`Text`](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Text) (caixas de entrada), [`Button`](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Button) (botões de ação) e [`Output`](https://ipywidgets.readthedocs.io/en/stable/examples/Output%20Widget.html) (áreas de exibição).
  - Organização do layout usando [`VBox`](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#VBox) (caixas verticais) e [`HBox`](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#HBox) (caixas horizontais).
  - Associação de eventos (cliques de botão) a funções Python.

- **[14.3 ARQUITETURA DO PROJETO (CRUD COM POO)](https://docs.python.org/pt-br/3/tutorial/classes.html)**: 
  - Modelagem do problema: Criação da classe `Contato` (dados) e da classe `Agenda` (lógica de negócios e persistência).
  - Implementação das operações **CRUD**: **C**reate (Criar), **R**ead (Ler/Listar), **U**pdate (não implementado neste desafio, mas sugerido como próximo passo), **D**elete (Deletar).
  - Encapsulamento do tratamento de erros e da leitura/escrita do JSON dentro dos métodos da classe, unindo os Módulos 11, 12 e 13.
