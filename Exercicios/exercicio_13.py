"""
1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""

def dobro(numero):
    """
    Função que recebe um número inteiro e devolve o seu dobro.
    :param numero: int
    :return: int
    """
    return numero * 2

# Programa principal
if __name__ == "__main__":
    numero = int(input("Digite um número inteiro: ")) # Solicita ao usuário um número inteiro
    resultado = dobro(numero) # Calcula o dobro utilizando a função

print(f"O dobro de {numero} é {resultado}.") # Exibe o resultado
