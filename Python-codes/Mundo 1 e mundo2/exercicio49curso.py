print("""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando o laço for. """)


tabuada = int(input("Qual tabuada deseja visualizar?\n"))

for i in range(0, 11):
    print("{} x {} = {}".format(tabuada, i, i * tabuada))
