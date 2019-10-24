print("""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
No final, mostre:
A) Quantas pessoas foram cadastradas 
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves""")
listalista = []
lista = []
pesados = []
resp = 'S'
c = d = 0

while resp != "N":
    lista.append(input("Informe o nome:\n"))
    lista.append(int(input("Informe o peso:\n")))
    listalista.append(lista[:])
    lista.clear()
    resp = input("Deseja continuar? [S/N]\n").upper()
    c += 1

for pos, pessoa in enumerate(listalista):
    for poss, dado in enumerate(pessoa):
        print(f'o dado é {dado} e está na posição {poss} da lista {pos}')
        print(dado[pos][poss])


