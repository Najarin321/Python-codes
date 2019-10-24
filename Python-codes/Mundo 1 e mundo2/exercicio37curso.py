print("""
Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão: 
- 1 para binário
- 2 para octal
- 3 para hexadecimal""")

num = int(input("Informe um número:\n"))

base_con = int(input("""Seleciona qual base de conversão deseja utilizar:
1 - Binário
2 - Octal
3 - Hexadecimal\n"""))

if base_con == 1:
    bina = bin(num)
    print(bina)
elif base_con == 2:
    octa = oct(num)
    print(octa)
else:
    hexa = hex(num)
    print(hexa)
