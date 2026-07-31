# --- Classe Pai ---
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        print(f"{self.nome} está comendo.")

# --- Classe Filha ---
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade) # Chama o construtor da classe pai
        self.raca = raca

    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

# --- Testes ---
meu_cao = Cachorro("Rex", 5, "Pastor Alemão")

meu_cao.comer()  # Método herdado de Animal
meu_cao.latir()  # Método exclusivo de Cachorro
