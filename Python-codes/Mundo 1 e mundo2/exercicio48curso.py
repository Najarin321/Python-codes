print("""
Faça um programa que calcule a soma entre todos os números 
ímpares que são múltiplos de três e que se encontram no intervalo
de 1 até 500""")

c = 0
for i in range(1,501):
    if i % 3 == 0:
        c += i
print(c)