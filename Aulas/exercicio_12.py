"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.
"""

sacola = []
produto = ''

print('Em nossa loja, a compra mínima é de 10 itens, não adianta chorar, ta duro vá pra casa!')
while len(sacola) < 10:
    print(f'Insira o produto {len(sacola) + 1}/10 no carrinho: ')
    produto = input()
    sacola.append(produto)
    if len(sacola) == 10:
        print('Por motivos que não posso explicar nosso mercado só pode vender 10 produtos por cliente ao dia, '
              'por favor, digite: "Sair"')
        resposta = input()
        while resposta != 'Sair':
            print('Por favor, digite Sair e retire-se!')
            resposta = input()

if len(sacola) >= 10:
    print(f'Sua sacola com: {sacola} está completa, agora por favor, PAGUE O QUE NOS DEVE!')