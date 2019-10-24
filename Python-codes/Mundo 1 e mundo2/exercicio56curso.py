print("""
Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre: 
A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos'
""")

for i in range(0,4):
    nome = input("Informe o nome do usuário:\n")
    sexo = input("Informe o seu sexo:\n")
    idade = int(input("Informe a sua idade:\n"))
    total_idade = total_idade + idade

media_idade = total_idade / 4
