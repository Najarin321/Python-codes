#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do 
#seno, cosseno e tangente desse ângulo

import math

angulo = int(input("Informe o ângulo que deseja: \n"))

cosseno = math.cos(angulo)
seno = math.sin(angulo)
tangente = math.tan(angulo)

print("Os respectivos valores de seno, cosseno e tangente são: \n {} \n {} \n {}".format(seno, cosseno, tangente))