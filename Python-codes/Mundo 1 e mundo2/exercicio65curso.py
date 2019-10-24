print("""
Crie um programa que leia vários números inteiros pelo teclado. No final
da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores""")

c = 0
maior_valor = 0 
menor_valor = 99999999
acumu = 0
resp = 'S'

while resp != "N":
    num = int(input("Informe um valor:\n"))
    acumu += num
    if maior_valor < num:
        maior_valor = num
    if menor_valor > num:
        menor_valor = num 
    c += 1 
    resp = input("Deseja continuar inserindo valores?\n").upper()

media = acumu / c

print("Maior valor lido: {}. Menor valor lido: {}".format(maior_valor,menor_valor))
print("Média {}".format(media))