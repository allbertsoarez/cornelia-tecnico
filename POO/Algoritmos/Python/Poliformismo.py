class Animal:
    def emitir_som(self):
        pass # Método base vazio

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# --- Testes (O "Pulo do Gato" do Polimorfismo) ---
# Criamos uma lista genérica contendo objetos de classes diferentes
animais = [Cachorro(), Gato()]

print("Executando o método emitir_som() em objetos diferentes:")
for animal in animais:
    # A mesma chamada, mas o Python executa a versão específica de cada objeto
    animal.emitir_som()
