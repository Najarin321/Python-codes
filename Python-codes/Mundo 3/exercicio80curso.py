print("""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela""")

listosa = []
for i in range(0,5):
    try:
        num = (int(input("Informe um valor:\n")))
    except ValueError:
        print("Digite um valor correto.")
    if i == 0 or num > listosa[len(listosa) - 1]:
        listosa.append(num)
    else:
        pos = 0
        while pos < len(listosa):
            if num <= listosa[pos]:
                listosa.insert(pos, num)
                break
            pos += 1
print("Os valores digitados em ordem foram: {}".format(listosa))
    

