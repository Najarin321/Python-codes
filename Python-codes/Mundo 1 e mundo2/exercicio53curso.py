print(""""
Crie um programa que leia uma frase qualquer e diga se ela é um 
palíndromo, desconsiderando os espaços""")

phrase = input("Informe uma frase:\n")

no_space = phrase.replace(" ", "").upper()

original = []

for char in no_space:
    original.append(char)

rever = list(reversed(original))

if rever == original:
    print("Palíndromo")
else:
    print("Não é um palíndromo")