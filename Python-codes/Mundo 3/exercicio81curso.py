print("""
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso,mostre: 

A) Quantos números foram digitados

B) A lista de valores, ordenada de forma decrescente 

C) Se o valor 5 foi digitado e está ou não na lista""")

listona = []
c = 0 
resp = 'S'
while resp != 'N':
    num = int(input("Informe um valor a ser adicionado:\n"))
    c += 1
    listona.append(num)
    resp = input("Deseja continuar? [S/N]\n").upper()
    

listona.sort(reverse=True)  

try: 
    five = listona.index(5)
except ValueError:
    print("Não identifiquei o valor 5")

if 5 in listona:
    print("O valor 5 foi digitado e foi encontrado na posição {}".format(five))

print("Você digitou uma quantidade de {} valores nessa lista".format(c))
print('Em ordem decrescente: {}'.format(listona))