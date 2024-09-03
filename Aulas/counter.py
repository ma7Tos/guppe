"""
Módulo Collections - Counter

Collections -> High-performance Container Datatype

Counter - > Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 5, 3, 45, 45, 6, 6, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 2, 45: 2, 6: 2, 43: 1, 34: 1})

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou no valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3

texto = '""… em 11 de setembro de 2001, o iG, então o maior portal informativo do Brasil, promovia o
"Dia da Boa Notícia", uma campanha em que só divulgava fatos positivos, e teve de cancelá-lo por conta dos atentados
 terroristas contra as Torres Gêmeas, em Nova York?""'

palavras = texto.split()
# print(palavras)
res = Counter(palavras)
# print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(3))
"""
