from abc import ABC, abstractmethod

# --- Classe Abstrata ---
class Veiculo(ABC):
    def __init__(self):
        self.velocidade_atual = 0

    @abstractmethod
    def mover(self):
        pass # Método abstrato não tem corpo, obriga as filhas a implementarem

# --- Classes Concretas ---
class Aviao(Veiculo):
    def mover(self):
        print("O avião está decolando e voando pelos ares!")

class Submarino(Veiculo):
    def mover(self):
        print("O submarino está mergulhando e navegando submerso!")

# --- Testes ---
meu_aviao = Aviao()
meu_aviao.mover()

meu_sub = Submarino()
meu_sub.mover()

# --- O Erro da Abstração ---
# Descomente a linha abaixo e execute a célula para ver o TypeError:
# veiculo_generico = Veiculo()
# print("Isso nunca vai imprimir")