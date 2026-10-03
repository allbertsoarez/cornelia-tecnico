### 15. [SAINDO DO NAVEGADOR (O MUNDO LOCAL)](https://docs.python.org/pt-br/3/using/index.html)
Neste módulo final, deixamos o Google Colab e configuramos o ambiente de desenvolvimento local (no próprio computador), preparando o aluno para criar aplicações desktop e scripts autônomos.

- **[15.1 INSTALAÇÃO DO PYTHON LOCAL](https://docs.python.org/pt-br/3/using/windows.html)**: 
  - Download da versão oficial em [python.org](https://www.python.org/downloads/).
  - A importância crítica de marcar a opção **"Add Python to PATH"** durante a instalação no Windows (o passo que mais causa dores de cabeça em iniciantes!).
  - Verificação da instalação via terminal (`python --version` ou `python3 --version`).

- **[15.2 O AMBIENTE DE DESENVOLVIMENTO (VS CODE)](https://code.visualstudio.com/docs/languages/python)**: 
  - Instalação do Visual Studio Code, o editor mais popular do mercado.
  - Instalação das extensões essenciais: **[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** (oficial da Microsoft) e **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** (para inteligência de código, *type hinting* e autocompletar).
  - Como selecionar o interpretador Python correto no VS Code (`Ctrl+Shift+P` > "Python: Select Interpreter").

- **[15.3 O TERMINAL E A EXECUÇÃO DE SCRIPTS](https://docs.python.org/pt-br/3/tutorial/interpreter.html#argument-passing)**: 
  - A diferença entre o ambiente interativo (REPL) e a execução de arquivos `.py` compilados em tempo de execução.
  - Como rodar um script pelo terminal (`python meu_script.py`).
  - O conceito de diretório de trabalho (*working directory*) e caminhos relativos para salvar arquivos JSON localmente de forma confiável.

- **[15.4 INTERFACES GRÁFICAS DESKTOP (TKINTER)](https://docs.python.org/pt-br/3/library/tkinter.html)**: 
  - O Tkinter é a biblioteca padrão do Python (*batteries included!*) para criar janelas, botões e campos de texto nativos do sistema operacional, sem necessidade de instalar pacotes externos.
  - O conceito de "Event Loop" ([`mainloop()`](https://docs.python.org/pt-br/3/library/tkinter.html#tkinter.mainloop)): O programa fica em um loop infinito esperando o usuário clicar ou digitar, diferente da execução linear de scripts.
  - Adaptação da arquitetura do Projeto Final: separando a Lógica de Negócios (Classe `Agenda`) da Interface Gráfica (Classe `App`), aplicando na prática o princípio de separação de responsabilidades.
