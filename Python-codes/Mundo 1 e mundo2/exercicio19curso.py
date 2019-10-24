#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

lista = ['Cleber','Johnson','Edmilson','Robson']

escolha = random.choice(lista)

print(escolha)