print(""""
Melhore o desafio 61, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra quando 
ele disser que quer mostrar 0 termos""")


num = int(input("Informe um valor:\n"))
reason = int(input("Qual será a diferença para o número anterior?\n"))
c = 0


while c < 10 :
    num += reason
    print(num)
    c += 1

resp = int(input("Deseja continuar? Se sim, informe quanto mais deseja incluir. (Digite 0 para sair): \t"))

if resp != 0:
    while c < 10 + resp:
        num += reason
        print(num)
        c +=1

