print(""" Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome \"Santo\"
""")

nome_cidade = input("Informe o nome da cidade: \n")
maiuscula = nome_cidade.upper()
quebra_nome = maiuscula.split()


if quebra_nome[0] == "santo".upper():
    print("Sua cidade começa com Santo :D")
else:
    print("Infelizmente sua cidade não começa com Santo :(")