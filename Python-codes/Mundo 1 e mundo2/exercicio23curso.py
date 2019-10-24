print("""
Exercício 24 - Faça um programa que leia de 0 a 9999 e mostre na tela 
cada um dos dígitos separados
""")

numero = int(input("Informe um valor de 0 a 9999:\n"))
while numero < 0 or numero > 9999:
    print("digite um número válido")
    numero = int(input("Informe um valor de 0 a 9999:\n"))

str_num = str(numero)

quebra_num = []
for num in str_num:
    quebra_num.append(num)


if len(quebra_num) == 4:
    milhar = quebra_num[0]
    print("Milhar: {}\n".format(milhar))
    centena = quebra_num[1]
    print("Centena: {}\n".format(centena))
    dezena = quebra_num[2]
    print("Dezena: {}\n".format(dezena))
    unidade = quebra_num[3]
    print("Unidade: {}\n".format(unidade))

elif len(quebra_num) == 3:
    centena = quebra_num[0]
    print("Centena: {}\n".format(centena))
    dezena = quebra_num[1]
    print("Dezena: {}\n".format(dezena))
    unidade = quebra_num[2]
    print("Unidade: {}\n".format(unidade))
elif len(quebra_num) == 2:
    dezena = quebra_num[0]
    print("Dezena: {}\n".format(dezena))
    unidade = quebra_num[1]
    print("Unidade: {}\n".format(unidade))
elif len(quebra_num) == 1:
    unidade = quebra_num[0]
    print("Unidade: {}\n".format(unidade))
else:
    print("there's nothing left to say :D")

#Não ficou um bom código, apesar de atender a solicitação 


