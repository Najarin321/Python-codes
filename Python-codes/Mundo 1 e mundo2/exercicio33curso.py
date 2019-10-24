print("""Faça um programa que leia três números e mostre qual é o maior
e qual é o menor
""")

vlr1 = int(input("Informe o primeiro valor:\n"))
vlr2 = int(input("Informe o segundo valor:\n"))
vlr3 = int(input("Informe o terceiro valor:\n"))

if vlr1 > vlr2:
    if vlr1 > vlr3:
        print("Primeiro valor é o maior")
    else:
        print("Terceiro valor é o maior")
else:
    if vlr2 > vlr3:
        print("Segundo valor é o maior")
    else:
        print("Terceiro valor é o maior")

