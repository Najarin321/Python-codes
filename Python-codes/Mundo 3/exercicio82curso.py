print("""
Crie um programa que vai ler vários números e colocar em uma lista. 

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente

Ao final, mostre o conteúdo das três listas geradas.
""")


list_total = []
list_par = []
list_impar = []

resp = "S"

while resp != "N":
    num = int(input("Informe um valor:\n"))
    list_total.append(num)
    if num % 2 == 0:
        list_par.append(num)
    else:
        list_impar.append(num)
    resp = input("Deseja continuar? [S/N]\n").upper()


print("Todos os números: {}".format(list_total))
print("Todos os números pares: {}".format(list_par))
print("Todos os números ímpares: {}".format(list_impar))