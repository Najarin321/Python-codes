print("""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
esteja errado, peça a digitação novamente até obter um valor correto""")

sexo = input("Informe o seu sexo: (M) para Masculino, (F) para feminino:\n").upper()

while sexo != 'M' and sexo != 'F':
    print("Por favor digite um valor correto!")
    sexo = input("Informe o seu sexo: (M) para Masculino, (F) para feminino:\n").upper()
