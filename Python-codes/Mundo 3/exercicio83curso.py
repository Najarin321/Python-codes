print("""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está 
com os parênteses abertos e fechados na ordem correta""")

expression = input("Digite a expressão:\n")

listosa = []

for i in expression:
    listosa.append(i)

count_open = listosa.count('(')
count_close = listosa.count(')')

if count_open == count_close:
    print("Essa expressão está correta")
else:
    print("Essa expressão está incorreta")