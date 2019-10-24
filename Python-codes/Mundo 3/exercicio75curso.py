print("""
Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares""")
c = 0
listosa = []
pares = []
for i in range(0,4):
    num = int(input("Informe um valor:\n"))
    listosa.append(num)

tuplosa = tuple(listosa)

for value in tuplosa: 
    if value == 9:
        c += 1
    if value % 2 == 0:
        pares.append(value)

localiza_3 = tuplosa.index(3)

print("O número 9 apareceu {} vezes".format(c))
print("O número 3 foi digitado na posição {}".format(localiza_3))
print("Esses foram os números pares digitados: {}".format(pares))

    