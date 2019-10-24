print("""
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado 
for ímpar, desconsidere-o""")
c = 0
for i in range (0,6):
    num = int(input("Informe um valor"))
    if num % 2 == 0:
        c += num 
print(c)