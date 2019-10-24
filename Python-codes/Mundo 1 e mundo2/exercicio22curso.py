print(""" Crie um programa que leia o nome completo de uma pessoa
e mostre: 
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas 
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
""")

nome = input("Informe o seu nome:\n")

maiuscula = nome.upper()
minuscula = nome.lower()
total_char = len(nome) - nome.count(" ")
quebra_nome = nome.split()
primeiro_nome = len(quebra_nome[0])


print(""" Esses são os dados retornados: 
Em maiúsculo: {}
Em minúsculo: {}
Total de letras: {}
Total de letras no primeiro nome: {}
""".format(maiuscula,minuscula,total_char,primeiro_nome))

#Não houve erro de código, lógica funcionou perfeitamente e de primeira. 

