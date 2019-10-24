print(""""
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while""")


num = int(input("Informe um valor:\n"))
reason = int(input("Qual será a diferença para o número anterior?\n"))
c = 0

while c < 10 :
    num += reason
    print(num)
    c += 1