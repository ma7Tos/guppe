"""
Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.
"""

vint: list[int] = []

while len(vint) < 6:
    valor: int = int(input(f'Informe o valor {len(vint) + 1}/6: '))
    vint.append(valor)

for valor in vint:
    print(valor)