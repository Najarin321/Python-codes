print("""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso 
o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em 
ordem crescente""")

numbers = []

resp = "S"

while resp != "N":
    num = int(input("Informe um valor:\n"))
    if not(num in numbers):
        numbers.append(num)
    else:
        print("Valor já existente, digite novamente")
    resp = input("Deseja inserir um novo valor?\n")

numbers.sort(reverse=True)

print(numbers)
