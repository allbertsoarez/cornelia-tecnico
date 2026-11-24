# Atividades práticas realizadas em sala

- [**Atividade em sala - Projeto: Modelagem de Jogos de Loteria**](https://colab.research.google.com/drive/1Zya_2KQQv6gdWVQEY1fichW7McLL-5wR?usp=sharing)<br>
Criar uma estrutura de classes para modelar jogos de loteria (Quina e Mega-Sena), utilizando herança e instanciação de objetos

    Abra o **Google Colab** e crie um novo notebook chamado `Projeto_Loteria_SeuNome.ipynb`.
  Organize seu código em **3 células de código** (como se fossem arquivos separados):

  📂 [**Célula 1: Classe Base - loteria.py**](https://colab.research.google.com/drive/1oRFaZtU8Ux8BS8aAxYhBXTktqd7o5dNY?usp=sharing)
  - Crie a classe `Loteria` com:
    - Método construtor `__init__(self, nome, total_dezenas)`
    - Atributos: `self.nome` e `self.total_dezenas`
    - Finalize com: `print("✅ Classe Loteria criada")`
    
  📂 [**Célula 2: Subclasses - jogos.py**](https://colab.research.google.com/drive/10FM1EnMOHUHo3lzdogLULboZPdKbHLXj?usp=sharing)
  - Crie duas classes que herdam de `Loteria`:
    - **Classe `Quina`:**
      - No `__init__`, use `super().__init__(nome="Quina", total_dezenas=5)`
    - **Classe `MegaSena`:**
      - No `__init__`, use `super().__init__(nome="Mega-Sena", total_dezenas=6)`
  - Finalize com: `print("✅ Subclasses criadas")`

  📂 [**Célula 3: Programa Principal - main.py**](https://colab.research.google.com/drive/1KDlMj4Oa-twbFB0v5-7cZ8tcRGZs3gCU?usp=sharing)
#### SLIDES
- [Slide 1 - Aula 3 - Classes, Instancia, Abstração](https://docs.google.com/presentation/d/1tj_XlMgPGlGz4jdLgup3Q89NCIPq2cya10xgvZypPRs/edit?usp=sharing)
