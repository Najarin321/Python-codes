print(""""
Faça um programa que leia um número qualquer e mostre seu fatorial.""")


number = int(input("Informe um número"))

count = number - 1

while count > 1:
    number *= count 
    count -= 1

print(number)