print(""""
Crie um programa que leia o nome de uma pessoa
e diga se ela tem \"Silva\" no nome.
""")

nome = input("Informe o seu nome: \n")
maiuscula = nome.upper()

localiza = maiuscula.find("SILVA") 

if localiza != -1: 
    print("Encontramos Silva em seu sobrenome")
else:
    print("Não encontramos Silva em seu sobrenome :C")

#Feito sem recorrer em ajuda, apesar de pensar em como usar a lógica booleana para o .find()



