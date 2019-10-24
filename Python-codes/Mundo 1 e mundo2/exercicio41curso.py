print("""
A confederação nacional de natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre
sua categoria de acordo com a sua idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Senior
- Acima 20 anos: Master """)

ano_nasc = int(input("Informe o seu ano de nascimento:\n"))
idade = 2019 - ano_nasc

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Senior")
else:
    print("Master")    