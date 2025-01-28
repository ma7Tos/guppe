"""
Listas Alinhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 2, 3, 4, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print(listas[0])

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1]) # 2
print(listas[2][1]) # 8

# Iterando com loops em uma lista alinhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[(print(valor)) for lista in listas for valor in lista]
"""

# Outros Exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jgadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])

