"""
Módulo Collections - Default Dict

# Recap Dicionários

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # Key Error
---------------------------------------------------------------------
Default Dict -> Ao criar um dicionário o utilizando, informamos um valor default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre qe não houver um valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será atribuído.

Obs.: Lambdas são funções sem nome, que podem ou não recever parâmetros de entrada e retornar valores.
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # Não dará Key Error.

print(dicionario)