print("""
Faça um programa que leia o nome completo de uma pessoa, mostrando em 
seguida o primeiro e o último nome separadamente
""")

nome = input("Informe o seu nome completo:\n")

quebra_nome = nome.split()
primeiro_nome = quebra_nome[0]
ultimo_nome = quebra_nome[-1]

print("Seu primeiro nome é: {}".format(primeiro_nome))
print("Seu último nome é {}".format(ultimo_nome))

#De fácil desenvolvimento. Sem erro logo na primeira vez. 