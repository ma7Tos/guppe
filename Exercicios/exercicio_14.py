"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.
"""

from datetime import datetime


def data_por_extenso(data_str):
    """
    Converte uma data no formato DD/MM/AAAA para o formato por extenso.
    :param data_str: str - Data no formato 'DD/MM/AAAA'
    :return: str - Data no formato 'D de mês de AAAA'
    """
    # Dicionário com os meses por extenso
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    try:
        # Converte a string para um objeto datetime
        data = datetime.strptime(data_str, "%d/%m/%Y")
        dia = data.day
        mes = meses[data.month - 1]  # Obtém o mês correspondente
        ano = data.year

        return f"{dia} de {mes} de {ano}"
    except ValueError:
        return "Data inválida! Use o formato DD/MM/AAAA."


# Programa principal
if __name__ == "__main__":
    data_input = input("Digite uma data no formato DD/MM/AAAA: ")
    resultado = data_por_extenso(data_input)
    print(resultado)
