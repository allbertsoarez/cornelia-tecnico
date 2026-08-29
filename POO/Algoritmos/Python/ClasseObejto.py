# --- Definição da Classe ---
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def ligar(self):
        print(f"O {self.modelo} {self.cor} está ligado! Vrum!")

# --- Criação do Objeto (Instanciação) ---
meu_carro = Carro("Azul", "Fusca")

# --- Execução ---
meu_carro.ligar()