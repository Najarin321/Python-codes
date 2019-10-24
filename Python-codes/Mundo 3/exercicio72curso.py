print("""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.""")

num_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", 
"dez", "onze", "doze", "treze", "quatorze",
 "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


num = int(input("Informe um número entre 0 e 20:\n"))

while num < 0 or num > 20:
    print("Por favor digite número válido!")
    num = int(input("Informe um número entre 0 e 20:\n"))

print(num_extenso[num])
