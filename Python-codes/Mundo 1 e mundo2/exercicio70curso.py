print("""
Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato""")

total_compra = 0
acima_mil = 0
valor_produto = 0
valor_produto_barato = 999999
d = ''

continua = 'S'
while continua == "S":
    nome_produto = input("Qual é o nome do produto?\n")
    valor_produto = int(input("Informe o valor de {}:\n".format(nome_produto)))
    if valor_produto > 1000:
        acima_mil += 1
    if valor_produto_barato > valor_produto:
        valor_produto_barato = valor_produto
        d = nome_produto
    
    total_compra += valor_produto
    continua = input("Deseja continuar? [S/N]\n").upper()

print("Você gastou {} em compras.".format(total_compra))
print("{} produtos custam mais do que R$1000,00".format(acima_mil))
print("O produto mais barato é {}".format(d))