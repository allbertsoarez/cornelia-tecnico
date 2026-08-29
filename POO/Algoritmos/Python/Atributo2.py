```python
class Aluno:
    total_alunos = 0  # atributo de classe

    def __init__(self, nome, nota=0.0):
        self.nome = nome       # atributo de instância
        self.nota = nota       # atributo de instância
        Aluno.total_alunos += 1
```
