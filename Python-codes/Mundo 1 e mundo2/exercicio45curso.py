import random
from time import sleep
print("""
Crie um programa que faça o computador jogar jokenpo com você""")

def jokenpo():
    minha_escolha = input("""Digite uma opção:
    - Papel
    - Pedra
    - Tesoura\n""").upper()
    possibilidades = ['PAPEL','TESOURA','PEDRA']
    escolha_maquina = random.choice(possibilidades)

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    
    print("O computador jogou {}".format(escolha_maquina))
    if minha_escolha == "PAPEL":
        if escolha_maquina == "TESOURA":
            print("Você perdeu!")
        elif escolha_maquina == "PEDRA":
            print("Você ganhou!")
        else:
            print("Temos um empate")
    elif minha_escolha == "TESOURA":
        if escolha_maquina == "PEDRA":
            print("Você perdeu!")
        elif escolha_maquina == "PAPEL":
            print("Você ganhou!")
        else:
            print("Temos um empate")
    else:
        if escolha_maquina == "PAPEL":
            print("Você perdeu!")
        elif escolha_maquina == "TESOURA":
            print("Você ganhou!")
        else:
            print("Temos um empate")


jokenpo()

    
    