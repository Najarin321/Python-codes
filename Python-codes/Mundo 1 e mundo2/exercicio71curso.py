print("""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10, e R$1""")


cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

resp = 'S'
while resp == 'S': 
    saque = int(input("Informe o valor para saque:\n"))

    while saque >= 50:
        saque -= 50
        cedula_50 += 1
    
    while saque >= 20:
        saque -= 20
        cedula_20 += 1

    while saque >= 10:
        saque -= 10
        cedula_10 += 1

    while saque >= 1:
        saque -= 1
        cedula_1 += 1

    print("""
    Você receberá:
    {} notas de 50 ;
    {} notas de 20 ;
    {} notas de 10;
    {} notas de 1.""".format(cedula_50,cedula_20,cedula_10,cedula_1))
    
    resp = input("Deseja efetuar um novo saque?\n").upper()
    

        
    
    