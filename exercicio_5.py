import math

print("De qual número você quer a Raiz Quadrática?")

n1 = int(input())

if n1 >= 0:
    raiz_quadrada = math.sqrt(n1)
    print("A raiz quadrada de", n1, "é: ", raiz_quadrada)
else:
    print("Não é possível descobrir a raiz quadrada de um número negativo.")

