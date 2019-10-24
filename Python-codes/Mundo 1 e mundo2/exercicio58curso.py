print("""
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. 
""")

import random

def jogo_advinha(dificuldade):
    numeros = random.randint(0,dificuldade)
    numero_usuario = int(input("Informe um valor entre 0 e {}:\n".format(dificuldade)))

    while numero_usuario < 0 or numero_usuario > dificuldade:
        print("Digite um valor válido!")
        numero_usuario = int(input("Informe um valor entre 0 e {}:\n".format(dificuldade)))
    
    while numero_usuario != numeros:
        numero_usuario = int(input("Informe um valor entre 0 e {}:\n".format(dificuldade)))        
    else:
        print("O número que eu pensei foi {}. Muito bem!".format(numeros))


dificuldade = int(input("""
    Informe a quantidade de números:
    - Fácil (0 - 20)
    - Médio (21 - 50)
    - Difícil ()51+"""))

jogo_advinha(dificuldade)