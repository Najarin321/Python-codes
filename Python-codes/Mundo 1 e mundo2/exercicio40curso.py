print("""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida: 
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado""")

nota1 = int(input("Informe o valor da primeira nota:\n"))
nota2 = int(input("Informe o valor da segunda nota:\n"))

media = (nota1 + nota2) / 2

if media < 5:
    print("reprovado")
elif media == 5 or media < 6.9:
    print("recuperação")
else:
    print("Aprovado")

