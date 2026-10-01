### 12. Arquivos e Tratamento de Erros
Neste módulo, saímos da memória volátil e aprendemos a interagir com o sistema de arquivos, além de construir programas robustos que não quebram diante de imprevistos.

- **12.1 Manipulação de Arquivos**: 
  - A função `open()` e os modos de abertura: `r` (leitura), `w` (escrita/sobrescrita) e `a` (append/adicionar ao final).
  - O bloco `with open(...) as ...`: O "gerenciador de contexto" que garante que o arquivo será fechado corretamente, mesmo que ocorra um erro durante a leitura/escrita.
  - A importância da codificação `utf-8` para suportar acentos e caracteres especiais.

- **12.2 Tratamento de Exceções (Erros)**: 
  - A filosofia do "Try/Except": Tentar executar um código e "pegar" o erro se ele acontecer, evitando que o programa trave.
  - **Hierarquia de Erros**: Tratando exceções específicas (ex: `ValueError`, `FileNotFoundError`, `ZeroDivisionError`) em vez de usar um `except` genérico.
  - **Os blocos auxiliares**: 
    - `else`: Executado apenas se **nenhum** erro ocorrer no `try`.
    - `finally`: Executado **sempre**, independentemente de sucesso ou falha (ideal para limpezas e encerramentos).
