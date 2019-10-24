print("""Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem, cobrando 0,50 por Km
para viagens de até 200km, e 0,45 para viagens mais longas.
""")

distancia_viagem = int(input("Qual é a distância da viagem desejada:\n"))

if distancia_viagem <= 200:
    valor = distancia_viagem * 0.50
else:
    valor = distancia_viagem * 0.45

print("Você deve pagar {}".format(valor))

