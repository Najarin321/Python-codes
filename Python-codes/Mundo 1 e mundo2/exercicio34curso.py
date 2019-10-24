print("""Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Aumento de 10% acima de 1250
aumento de 15% abaixo de 1250
""")

sal_atual = int(input("Informe o seu salário:\n"))

if sal_atual > 1250:
    sal_novo = (sal_atual * 0.10) + sal_atual
else:
    sal_novo = (sal_atual * 0.15) + sal_atual

print("Seu novo salárui será de R${}".format(sal_novo))