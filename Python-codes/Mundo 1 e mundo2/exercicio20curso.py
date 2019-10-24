#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada 

import random

lista = ['Cleber','Johnson','Edmilson','Robson']

random.shuffle(lista)

print(lista)