```java
public class Aluno {
    static int totalAlunos = 0; // atributo de classe
    String nome;                // atributo de instância
    double nota;               // atributo de instância

    public Aluno(String nome) {
        this.nome = nome;
        totalAlunos++;
    }
}
```