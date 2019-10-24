#Faça um programa que leia o comprimento do cateto oposto e do 
#cateto adjacente de um triângulo retângulo, calcule 
#e mostre o comprimento da hipotenusa

import math

cat_opo = int(input("Informe o cateto oposto: \n"))
cat_adj = int(input("Informe o cateto adjacente: \n"))

hipotenusa = math.hypot(cat_opo, cat_adj)
print("A hipotenusa desse triângulo é aproximadamente: {}".format(int(hipotenusa)))