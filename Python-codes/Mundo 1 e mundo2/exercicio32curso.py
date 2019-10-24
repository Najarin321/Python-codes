print("""Faça um programa que leia um ano qualquer e mostre se ele é 
bissexto
""")

ano_bissexto = int(input("Informe um ano:\n"))

if ano_bissexto % 4 == 0:
    print("Ano bissexto!")
else:
    print("Ano normal")

