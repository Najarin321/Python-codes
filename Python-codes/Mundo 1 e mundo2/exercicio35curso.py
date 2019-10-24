print("""Desenvolva um programa que leia o comportamento de 
três retas e diga ao usuário se elas podem ou não formar um triângulo.
""")

a = int(input("Informe o comprimento da primeira reta:\n"))
b = int(input("Informe o comprimento da segunda reta:\n"))
c = int(input("Informe o comprimento da terceira reta:\n"))

if a < b + c and b < a + c and c < a + b:
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")
    
     