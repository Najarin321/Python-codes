print("""
Faça um programa que leia 5 valores numéricos e guarde em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na tela. """)

numbers = []

c = 0

while c < 5:
    num = int(input("Informe um número:\n"))
    numbers.append(num)
    c += 1

#for pos, number in enumerate(numbers):


maior = max(numbers)
menor = min(numbers)

maior_pos = numbers.index(max(numbers))
menor_pos = numbers.index(min(numbers))

print("O maior valor encontrado foi {}, que está na posição {}. \nO menor valor encontrado foi {}, que está na posição {}".format(maior, maior_pos, menor,menor_pos))