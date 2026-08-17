´´´

// ==========================================
// 1. A CLASSE (O Molde / A Planta)
// ==========================================
class Celular {
    
    // --- ATRIBUTOS (As características / O estado do objeto) ---
    String marca;
    String cor;
    int nivelBateria; // De 0 a 100


    // --- MÉTODOS (As ações / O que o objeto sabe fazer) ---
    
    // Método para tirar uma foto (Gasta bateria)
    void tirarFoto() {
        System.out.println("📸 Clic! Foto tirada com o " + marca + ".");
        nivelBateria -= 5; // Diminui 5% de bateria
    }

    // Método para carregar o celular
    void carregar() {
        System.out.println("🔌 Carregando o " + marca + " na tomada...");
        nivelBateria = 100; // Bateria volta a 100%
    }

    // Método para mostrar o status atual
    void mostrarStatus() {
        System.out.println("📱 Status: " + marca + " (" + cor + ") | Bateria: " + nivelBateria + "%");
    }
}


// ==========================================
// 2. ONDE CRIAMOS O OBJETO (O Mundo Real)
// ==========================================
public class Main {
    public static void main(String[] args) {
        
        // --- CRIANDO O OBJETO ---
        // Estamos tirando o celular do molde e dando um nome a ele na memória
        Celular meuCelular = new Celular(); 
        Celular celularDaMaria = new Celular(); // Podemos criar quantos quisermos!


        // --- USANDO OS ATRIBUTOS (Definindo as características) ---
        meuCelular.marca = "Samsung";
        meuCelular.cor = "Preto";
        meuCelular.nivelBateria = 80;

        celularDaMaria.marca = "Apple";
        celularDaMaria.cor = "Rosa";
        celularDaMaria.nivelBateria = 50;


        // --- USANDO OS MÉTODOS (Executando as ações) ---
        System.out.println("--- Ações do MEU celular ---");
        meuCelular.mostrarStatus();
        
        meuCelular.tirarFoto(); // A bateria vai cair!
        meuCelular.mostrarStatus(); // Vamos ver a bateria nova
        
        meuCelular.carregar();
        meuCelular.mostrarStatus(); // Bateria deve estar em 100% agora


        System.out.println("\n--- Ações do celular da MARIA ---");
        celularDaMaria.mostrarStatus();
        celularDaMaria.tirarFoto();
        celularDaMaria.mostrarStatus();
    }
}
´´´