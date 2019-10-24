print("""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular""")

tuplosa = ('Cachorro', 2000,'pedra', 5,'macaco',300,'monkey',25,'brasil',10000,'vento', 10)

for string in range(0, len(tuplosa)):
    if string % 2 == 0:
        print(f'{tuplosa[string]:.<30}', end = '')
    else:
        print(f'{tuplosa[string]:>7.2f}')

