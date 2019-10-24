print(""""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma 
sequência de Fibonacci""")

a = 0
b = int(input("Informe um valor:"))
c = 0
qtd = int(input("Quantos valores deseja mostrar?\n"))

while qtd > 0: 
    a = b
    b = c
    c = a + b
    print(b)
    qtd -= 1