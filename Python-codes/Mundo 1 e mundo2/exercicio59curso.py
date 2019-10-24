print("""
Crie um programa que leia dois valores e mostre um menu na tela: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] Sair do programa
 """)

menu = 4

while menu != 5:
    if menu == 1:
        soma = num1 + num2
        print("O resultado da soma é: {}\n".format(soma))
    elif menu == 2:
        mult = num1 * num2
        print("O resultado da multiplicação é: {}\n".format(mult))
    elif menu == 3:
        if num1 > num2:
            print("Primeiro número é maior\n")
        else:
            print("Segundo número é maior\n")
    elif menu == 4:
        num1 = int(input("Informe o primeiro valor:\n"))
        num2 = int(input("Informe o segundo valor:\n"))
    menu = int(input(""" Selecione uma das opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] novos números
    [5] Sair do programa\n\n"""))

print("Obrigado! Até a próxima")

