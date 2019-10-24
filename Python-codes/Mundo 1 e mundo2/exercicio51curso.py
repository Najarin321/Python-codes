print("""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão. """)

num = int(input("Informe um valor:\n"))
reason = int(input("Qual será a diferença para o número anterior?\n"))
c = 0
for i in range(0,10):
    num += reason
    print(num)
 