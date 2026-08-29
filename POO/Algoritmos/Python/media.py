# =========================================================
# Programa: Calculadora de Média (Abordagem Estruturada)
# =========================================================

def calcular_media(lista_de_valores):
    """
    Função (AÇÃO): Recebe uma lista de números, soma todos 
    e divide pela quantidade para retornar a média.
    """
    soma = 0
    # Percorrendo cada valor na lista
    for valor in lista_de_valores:
        soma += valor  # Acumulador
    
    # Calculando a média (soma / quantidade de elementos)
    media = soma / len(lista_de_valores)
    return media


def main():
    """
    Função principal: Orquestra a execução do programa.
    É aqui que definimos o fluxo de cima para baixo.
    """
    print("--- Cálculo de Média Aritmética ---")
    print("Por favor, digite 5 valores.\n")

    # 1. Coletando os dados (os valores ficam soltos, guardados numa lista)
    valores = []
    for i in range(5):
        nota = float(input(f"Digite o {i+1}º valor: "))
        valores.append(nota)

    # 2. Processando os dados (chamando a função de ação)
    resultado = calcular_media(valores)

    # 3. Exibindo o resultado
    print("\n--- Resultado ---")
    print(f"A média aritmética dos 5 valores é: {resultado:.2f}")


# Ponto de entrada do programa (Boa prática em Python estruturado)
if __name__ == "__main__":
    main()