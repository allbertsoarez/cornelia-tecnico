# SEMANA 1
#### 📖 ATIVIDADES
- [Lista de Exercícios - Aula 1](https://docs.google.com/forms/d/e/1FAIpQLSdnFpzgdQIs1de1Br8LQutuQHC0UzoGdfS0RhM8h7Yw_SND6g/viewform?usp=dialog)
#### SLIDES
- [Slide 1 - Introdução a POO](https://docs.google.com/presentation/d/1olzUcprzTvNhBGMIrnUIdwRL0bk03WytnBVvl3Epwrg/edit?usp=sharing)
- [Slide 2 - Programação Orientada à Objetos](https://docs.google.com/presentation/d/1LQMvN5KJPGPLnSVE2OyQxPt1vITSEeSP_--s9cUT3qg/edit?usp=sharing)
- [Slide 3 - Programação Estruturada vs POO](https://docs.google.com/presentation/d/1yiO-QOv0fNWJwqhgl6ncSyrGxhqqaoZzIezBv6lDLLs/edit?usp=sharing)
#### COLAB NOTEBOOKS
- [Introdução à POO, algoritmos em Portugol e Python](https://colab.research.google.com/drive/1jMTQIDfhTYLMSxu5YOJG3WPmT7rjOA5n?usp=sharing)
- [Explicando POO com Python](https://colab.research.google.com/drive/1yyjfTD7EM70BI0hv--6kOiAL9gVwRyjD?usp=sharing) 
---
# SEMANA 2
#### 📖 ATIVIDADES
- [Lista de Exercícios 1 - Aula 2](https://docs.google.com/forms/d/e/1FAIpQLSd9-XONQHVRIORF6YT_cwqYzUeNnhO_nQKmaikV7uGH14wB0g/viewform?usp=header)
- [Lista de Exercícios 2 - Aula 2](https://docs.google.com/forms/d/e/1FAIpQLSefDvfYOyZ7Xd8JpGFvVDVqTlO9STVPzhx0p1nx7dyLRiJQDg/viewform?usp=header)
- [Lista de Exercícios 3 - Aula 2](https://docs.google.com/forms/d/e/1FAIpQLSdbgIBz8yiqJPtNEboa96wfgFxulws-gHmQCgrR_dhl-djQKQ/viewform?usp=header)
#### SLIDES
- [Do molde a realidade](https://docs.google.com/presentation/d/1iySks-yJcqlp1LRaVJw-mC-scWtp_3pqAxzQMkO7E3s/edit?usp=sharing)
- [A lógica da percepção humana](https://docs.google.com/presentation/d/1rrToEkZPlR6S8dOVDi-iCrG04ZgZoX2_Z5VaPPao-Vw/edit?usp=sharing)
#### COLAB NOTEBOOKS
- [Fundamentos](https://colab.research.google.com/drive/1sPrZ-UmILHaA8lj2xhxIw3IwIDLV3Z8E?usp=sharing)
- [Objetos, Atributos e Métodos](https://colab.research.google.com/drive/12OMIavJiclxPuQGYDQlTxpOeKxPC53Nf?usp=sharing)
- [Programação Estruturada vs POO](https://colab.research.google.com/drive/1XKoXB7r6tVmEOOh-RSagQ_cp_kC_OFQM?usp=sharing)
- [Pilar 1 - ABSTRAÇÃO](https://colab.research.google.com/drive/1h2Ml-fFRPbHnv3LV4LLCjIoi9jiSJHp7?usp=sharing)
- [Pilar 2 - ENCAPSULAMENTO1](https://colab.research.google.com/drive/1zmZhH8DYYoZ3o_qwg0Qn7_I0llUXKidL?usp=sharing)
- [Pilar 2 - ENCAPSULAMNETO2](https://colab.research.google.com/drive/1mu4wZXJI8MlaXcODqrGLxq3-prb--WQ7?usp=sharing)
- [Pilar 3 - HERANÇA](https://colab.research.google.com/drive/1R8CYie5i20uMp5dbfO2MXZevAgynlJ1I?usp=sharing)
- [Pilar 4 - POLIFORMISMO](https://colab.research.google.com/drive/1NBO8MSXugg_EH3_dx5nQApt9QWLpQf1P?usp=sharing)
---
# SEMANA 3

#### 📖 ATIVIDADES
- [Lista de Exercício 1 - Aula 3](@BnsShpaTJYrGdeuQnvSLih^Lt2Rkv*JbgT59&nm^Ff3dTyMzcMNZe6ThVjzc!96PcESfu)

- **Atividade em sala - Projeto: Modelagem de Jogos de Loteria**
  Criar uma estrutura de classes para modelar jogos de loteria (Quina e Mega-Sena), utilizando herança e instanciação de objetos

    Abra o **Google Colab** e crie um novo notebook chamado `Projeto_Loteria_SeuNome.ipynb`.
  Organize seu código em **3 células de código** (como se fossem arquivos separados):

  📂 [**Célula 1: Classe Base (`loteria.py`)**](https://colab.research.google.com/drive/1oRFaZtU8Ux8BS8aAxYhBXTktqd7o5dNY?usp=sharing)
  - Crie a classe `Loteria` com:
    - Método construtor `__init__(self, nome, total_dezenas)`
    - Atributos: `self.nome` e `self.total_dezenas`
    - Finalize com: `print("✅ Classe Loteria criada")`
    
  📂 **Célula 2: Subclasses (`jogos.py`)**
  - Crie duas classes que herdam de `Loteria`:
    - **Classe `Quina`:**
      - No `__init__`, use `super().__init__(nome="Quina", total_dezenas=5)`
    - **Classe `MegaSena`:**
      - No `__init__`, use `super().__init__(nome="Mega-Sena", total_dezenas=6)`
  - Finalize com: `print("✅ Subclasses criadas")`

  📂 **Célula 3: Programa Principal (`main.py`)**
#### SLIDES
- [Slide 1 - Aula 3 - Classes, Instancia, Abstração](https://docs.google.com/presentation/d/1tj_XlMgPGlGz4jdLgup3Q89NCIPq2cya10xgvZypPRs/edit?usp=sharing)
#### COLAB NOTEBOOKS
- [PARTE 1 - ESTRUTURA BÁSCIA DA CLASSES](https://colab.research.google.com/drive/1amowC1V-ug9A06DaQcU5r5OmADIKWfQw?usp=sharing)
- [PARTE 2 - O QUE É INSTANCIAÇÃO](https://colab.research.google.com/drive/1XMX55NQGviKNX3L_uRpaInohaEZDdVTz?usp=sharing)
- [PARTE 3 - CLASSE ABSTRATA](https://colab.research.google.com/drive/1lCIo2UcCb9c72sOshPoYIKihFtkXE8Mo?usp=sharing)
- [O MUNDO DAS LOTERIAS NA POO](https://colab.research.google.com/drive/1m_sI-p4bQCmA8jPU0Pzyyo0p2Ezu40ld?usp=sharing)
- [ATIVIDADE - LOTERIA - TODAS AS CÉLULAS](https://colab.research.google.com/drive/1Zya_2KQQv6gdWVQEY1fichW7McLL-5wR?usp=sharing)



- [ATIVIDADE - LOTERIA - CÉLULA 2 - Explicando o arquivo jogos.py](https://colab.research.google.com/drive/10FM1EnMOHUHo3lzdogLULboZPdKbHLXj?usp=sharing)
- 

---

# RECOMENDAÇÕES

#### SOFTWARES
- [VS CODE - Ver WEB](https://vscode.dev/?vscode-lang=pt-br)
- [Google Colab - Para rodar scripts Python](https://colab.research.google.com/)
- [Coddy Tech](https://coddy.tech/playground/pt/c)
 
