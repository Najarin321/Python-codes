print(""""
Faça um programa que leia o peso de cinco pessoas. No final, 
mostre qual foi o maior e o menor peso lidos. """)
c = 0
d = 9999
for i in range(0,5):
    peso = int(input("Informe o seu peso:"))
    if peso > c:
        c = peso
    if d > peso:
        d = peso

print("O maior peso foi {}".format(c))
print("O menor peso foi {}".format(d))