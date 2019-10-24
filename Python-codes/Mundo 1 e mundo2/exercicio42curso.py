print("""Refaça o desafio 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
""")

a = int(input("Informe o comprimento da primeira reta:\n"))
b = int(input("Informe o comprimento da segunda reta:\n"))
c = int(input("Informe o comprimento da terceira reta:\n"))

if a < b + c and b < a + c and c < a + b:
    print("Forma um triângulo")
    if a == b:
        if a == c:
            print("Equilatero")
    else:
        if b == c:
            print("Isósceles")
        else:
            print("Escaleno")
else:
    print("Não forma um triângulo")


     