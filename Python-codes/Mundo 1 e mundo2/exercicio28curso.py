print("""Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 a 5 e peça ao usuário tentar descobrir 
qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
""")

import random

def jogo_advinha(dificuldade):
    numeros = random.randint(0,dificuldade)
    numero_usuario = int(input("Informe um valor entre 0 e {}:\n".format(dificuldade)))

    while numero_usuario < 0 or numero_usuario > dificuldade:
        print("Digite um valor válido!")
        numero_usuario = int(input("Informe um valor entre 0 e {}:\n".format(dificuldade)))
    
    if numero_usuario == numeros:
        print("O número que eu pensei foi {}. Muito bem!".format(numeros))
    else:
        print("O número que eu pensei foi {}. Tente novamente!".format(numeros))
        resp = input("Deseja tentar novamente?\n").upper()
        if resp == "S":
            jogo_advinha(dificuldade)
        else:
            print("Até a próxima!")


dificuldade = int(input("""
    Informe a quantidade de números:
    - Fácil (0 - 20)
    - Médio (21 - 50)
    - Difícil ()51+"""))

jogo_advinha(dificuldade)

