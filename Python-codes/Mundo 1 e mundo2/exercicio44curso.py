print("""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto 
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros """)

valor_prod = int(input("Informe o valor do produto:\n"))
forma_pagto = int(input("""Informe a forma de pagamento:
1 - À vista dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão\n"""))

if forma_pagto == 1:
    valor_novo = valor_prod - valor_prod * 0.1 
    print("Você pagará o total de {} por esse produto.".format(valor_novo))
elif forma_pagto == 2:
    valor_novo = valor_prod - valor_prod * 0.05 
    print("Você pagará o total de {} por esse produto.".format(valor_novo))
elif forma_pagto == 3:
    print("Você pagará o total de {} por esse produto, em duas parcelas fixas.".format(valor_prod))
elif forma_pagto == 4:
    valor_novo = valor_prod + valor_prod * 0.05
    print("Você pagará o total de {} por esse produto, em três parcelas fixas.".format(valor_novo))