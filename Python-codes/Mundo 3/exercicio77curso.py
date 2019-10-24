print("""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais""")

meu_cabare = ('Cavalo', 'Jamanta', 'Jacare', "Zebra caolha", "Girafa perneta")
i = 0
for word in meu_cabare:
    print("\nA palavra {} tem as seguintes vogais:".format(word), end ='')
    for char in word:
        if char in 'aeiou':
            print("{}".format(char), end =',')