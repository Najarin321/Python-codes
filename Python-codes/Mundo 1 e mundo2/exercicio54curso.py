print(""""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.""")

c = 0
d = 0
for i in range(0, 7):
    ano_nasc = int(input("Informe seu ano de nascimento:\n"))
    idade = 2019 - ano_nasc
    if idade < 18:
        c += 1
    else:
        d += 1
print("Um total de {} pessoas são menores de idade. Um total de {} atingiram a maioridade!".format(c,d))