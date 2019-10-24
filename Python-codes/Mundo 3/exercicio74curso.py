from random import randint

print("""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla """)

listons = []
for i in range(0, 5):
    num = randint(0, 70)
    listons.append(num)

tuplosa = tuple(listons)

print(tuplosa)

maior = 0
menor = 9999
for value in tuplosa:
    if maior < value:
        maior = value
    if menor > value:
        menor = value

print("O menor valor na tupla é {}".format(menor))
print("O maior valor na tupla é {}".format(maior))