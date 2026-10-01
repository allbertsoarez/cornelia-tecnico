### 13. O Formato JSON
Neste módulo, aprendemos a trabalhar com o formato de dados mais popular da internet, permitindo salvar e carregar estruturas complexas (listas, dicionários) de forma estruturada.

- **13.1 O que é JSON**: 
  - JSON (JavaScript Object Notation) é um formato de texto leve para troca de dados.
  - É legível por humanos e fácil de parsear por máquinas.
  - Estruturas básicas: objetos (pares chave-valor, como dicionários) e arrays (listas ordenadas).

- **13.2 O Módulo `json` do Python**: 
  - `json.dump(dados, arquivo)`: Serializa (converte) um objeto Python em JSON e o escreve em um arquivo.
  - `json.load(arquivo)`: Desserializa (lê) um arquivo JSON e o converte de volta em um objeto Python.
  - `json.dumps(dados)`: Converte para JSON e retorna como string (útil para exibir na tela).
  - `json.loads(string)`: Converte uma string JSON em objeto Python.

- **13.3 Persistência de Dados Complexos**: 
  - Como salvar listas de dicionários (a estrutura básica de bancos de dados NoSQL).
  - Como carregar dados ao iniciar um programa para restaurar o estado anterior.
  - O padrão "carregar-modificar-salvar" para sistemas com estado persistente.
