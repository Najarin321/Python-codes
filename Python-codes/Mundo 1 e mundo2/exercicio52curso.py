print("""
Faça um programa que leia um número inteiro e diga 
se ele é ou não um número primo.""")


num = int(input("Informe um número:\n"))
tot = 0
for value in range(1,num +1):
    if num % value == 0:
        tot += 1

if tot == 2:
    print("É primo!")
else:
    print("Não é primo!")

