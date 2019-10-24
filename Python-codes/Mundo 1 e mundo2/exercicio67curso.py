print("""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo""")
c = 0
num = int(input("Informe um número"))
while True:
    mult = num * c 
    print("{} x {} = {}".format(num, c, mult))
    c += 1
    if c == 11:
        c = 0
        num = int(input("Informe um número"))
    if num < 0:
        break
    
#de primeira