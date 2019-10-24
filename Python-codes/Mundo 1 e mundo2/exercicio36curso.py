print("""
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode 
exceder 30% do salário ou então o empréstimo será negado.""")

valor_casa = int(input("Informe o valor da casa:"))
salario = int(input("Informe o seu salário:"))
quant_anos = int(input("Informe em quantos anos pretende pagar:"))

possivel_pagar = salario * 0.3
total_meses = quant_anos * 12
valor_mes = valor_casa / total_meses

if possivel_pagar > valor_mes:
    print("É possível comprar a casa")
else:
    print("Infelizmente não podemos financiar nesse valor :/")
