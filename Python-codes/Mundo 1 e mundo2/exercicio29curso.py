print(""""Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h, mostrar uma mensagem que ele foi multado. 
A multa vai custar R$7,00 para cada Km acima do limite
""")

velocidade = float(input("Informe a velocidade atingida:\n"))

velocidade_limite = 80

if velocidade > velocidade_limite:
    valor = (velocidade - velocidade_limite) * 7
    print("Você foi multado, deve pagar R${} de multa".format(valor))
else:
    print("Está tudo certo motorista, continue assim! :D")