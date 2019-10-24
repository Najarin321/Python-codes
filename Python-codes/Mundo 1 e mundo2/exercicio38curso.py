print("""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais""")

vlr1 = int(input("Informe o primeiro valor:\n"))
vlr2 = int(input("Informe o segundo valor:\n"))

if vlr1 > vlr2: 
    print("O primeiro valor é maior")
elif vlr2 > vlr1: 
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")