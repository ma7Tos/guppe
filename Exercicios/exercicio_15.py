"""
3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

def maior_valor(lista):
    """
    Função que recebe uma lista de inteiros e retorna o maior valor.
    :param lista: list - Lista de números inteiros
    :return: int - Maior valor da lista
    """
    if not lista:  # Verifica se a lista está vazia
        return "A lista está vazia!"
    return max(lista)  # Retorna o maior valor da lista

# Programa principal
if __name__ == "__main__":
    # Exemplo de lista
    numeros = [10, 25, 36, 12, 89, 74]
    # Chama a função
    maior = maior_valor(numeros)
    # Exibe o resultado
    print(f"O maior valor da lista é: {maior}")
