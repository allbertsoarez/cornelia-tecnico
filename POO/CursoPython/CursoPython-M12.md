### 12. [ARQUIVOS E TRATAMENTO DE ERROS](https://docs.python.org/pt-br/3/tutorial/inputoutput.html)
Neste módulo, saímos da memória volátil e aprendemos a interagir com o sistema de arquivos, além de construir programas robustos que não quebram diante de imprevistos.

- **[12.1 MANIPULAÇÃO DE ARQUIVOS](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files)**: 
  - A função [`open()`](https://docs.python.org/pt-br/3/library/functions.html#open) e os modos de abertura: `r` (leitura), `w` (escrita/sobrescrita) e `a` (append/adicionar ao final).
  - O bloco [`with open(...) as ...`](https://docs.python.org/pt-br/3/reference/compound_stmts.html#the-with-statement): O "gerenciador de contexto" que garante que o arquivo será fechado corretamente, mesmo que ocorra um erro durante a leitura/escrita.
  - A importância da codificação `utf-8` para suportar acentos e caracteres especiais do nosso idioma.

- **[12.2 TRATAMENTO DE EXCEÇÕES (ERROS)](https://docs.python.org/pt-br/3/tutorial/errors.html)**: 
  - A filosofia do [`try/except`](https://docs.python.org/pt-br/3/tutorial/errors.html#handling-exceptions): Tentar executar um código e "pegar" o erro se ele acontecer, evitando que o programa trave abruptamente.
  - **Hierarquia de Erros**: Tratando exceções específicas (ex: [`ValueError`](https://docs.python.org/pt-br/3/library/exceptions.html#ValueError), [`FileNotFoundError`](https://docs.python.org/pt-br/3/library/exceptions.html#FileNotFoundError), [`ZeroDivisionError`](https://docs.python.org/pt-br/3/library/exceptions.html#ZeroDivisionError)) em vez de usar um `except` genérico, o que é uma excelente prática de programação.
  - **Os blocos auxiliares**: 
    - [`else`](https://docs.python.org/pt-br/3/tutorial/errors.html#handling-exceptions): Executado apenas se **nenhum** erro ocorrer no `try`.
    - [`finally`](https://docs.python.org/pt-br/3/tutorial/errors.html#defining-clean-up-actions): Executado **sempre**, independentemente de sucesso ou falha (ideal para limpezas de memória, fechar arquivos e encerramentos).
