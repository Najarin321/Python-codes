print("""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos""")

c = 0
d = 0
e = 0
continua = 'S'
while continua == "S":
    idade = int(input("Informe a sua idade:\n"))
    sexo = input("Você é do sexo (M)asculino ou (F)eminino?\n").upper()
    if sexo == "F" and idade < 20:
        d += 1
    if sexo == "M":
        c += 1
    if idade > 18:
        e += 1
    continua = input("Deseja continuar?\n").upper()

print("Existem {} mulheres abaixo dos 20 anos nessa lista.".format(d))
print("{} homens foram cadastrados no sistema".format(c))
print("Ao todo {} usuários possuem mais de 18 anos".format(e))