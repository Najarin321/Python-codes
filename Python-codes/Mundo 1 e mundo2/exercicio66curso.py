print("""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário    
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles,exceto o 999""")
acumu = 0
c = 0
while True: 
    num = int(input("Informe um valor:"))
    if num == 999:
        break
    acumu += num
    c += 1
print("Foram digitados {} números".format(c))
print("A soma dos valores foi: {}".format(acumu))