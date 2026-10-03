### 13. [O FORMATO JSON](https://docs.python.org/pt-br/3/library/json.html)
Neste módulo, aprendemos a trabalhar com o formato de dados mais popular da internet, permitindo salvar e carregar estruturas complexas (listas, dicionários) de forma estruturada.

- **[13.1 O QUE É JSON](https://docs.python.org/pt-br/3/library/json.html)**: 
  - JSON (JavaScript Object Notation) é um formato de texto leve para troca de dados.
  - É legível por humanos e fácil de processar (parsear) por máquinas.
  - Estruturas básicas: objetos (pares chave-valor, idênticos aos dicionários do Python) e arrays (listas ordenadas).

- **[13.2 O MÓDULO `JSON` DO PYTHON](https://docs.python.org/pt-br/3/library/json.html)**: 
  - [`json.dump(dados, arquivo)`](https://docs.python.org/pt-br/3/library/json.html#json.dump): Serializa (converte) um objeto Python em JSON e o escreve diretamente em um arquivo.
  - [`json.load(arquivo)`](https://docs.python.org/pt-br/3/library/json.html#json.load): Desserializa (lê) um arquivo JSON e o converte de volta em um objeto Python.
  - [`json.dumps(dados)`](https://docs.python.org/pt-br/3/library/json.html#json.dumps): Converte para JSON e retorna como uma string (o "s" vem de *string*, útil para exibir na tela ou enviar por rede).
  - [`json.loads(string)`](https://docs.python.org/pt-br/3/library/json.html#json.loads): Converte uma string no formato JSON em um objeto Python (o "s" vem de *string*).

- **[13.3 PERSISTÊNCIA DE DADOS COMPLEXOS](https://docs.python.org/pt-br/3/library/json.html)**: 
  - Como salvar listas de dicionários (a estrutura básica de bancos de dados NoSQL e APIs modernas).
  - Como carregar dados ao iniciar um programa para restaurar o estado anterior (ex: configurações do usuário, histórico, etc).
  - O padrão "carregar-modificar-salvar" para sistemas com estado persistente, unindo tudo o que aprendemos sobre arquivos e dicionários.

cisar de ajuda para criar exercícios práticos, projetos finais para amarrar os conceitos, ou revisar qualquer outro material, é só chamar. Muito sucesso com as suas aulas, professor! 🚀🐍📚
