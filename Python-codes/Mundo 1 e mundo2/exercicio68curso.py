from random import randint

print("""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele consquistou no jogo.""")


perdeu = False
c = 0

while perdeu == False:
    
    system_input = randint(1, 100)
    user_input = int(input("Informe um valor:\n"))

    if user_input % 2 == 0:
        if (user_input + system_input) % 2 == 0:
            print("Você venceu")

        else: 
            print("Você perdeu, sua taxa de vitórias consecutivas foi {}".format(c))
            break
    else: 
        if (user_input + system_input) % 2 == 1:
            print("Você venceu")
            
        else:
            print("Você perdeu, sua taxa de vitórias consecutivas foi {}".format(c))
            break
    c += 1     

        





