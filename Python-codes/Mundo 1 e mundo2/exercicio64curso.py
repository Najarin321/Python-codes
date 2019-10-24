print("""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag) """)

number = 0
c = 0
soma = 0
while number != 999:
    number = int(input("Informe um valor:\n"))
    if number != 999:
        soma += number
        c += 1

print("O valor somado foi {}".format(soma))
print("Ao todo você incluiu {} valores".format(c))