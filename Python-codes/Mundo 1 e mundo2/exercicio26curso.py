print(""""Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra \"A\"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez. 
""")

frase = input("Cite uma frase bem conhecida: ")
frase_cima = frase.upper()
i = 0
todos_a = []
for letter in frase_cima:
    if letter == 'A':
        todos_a.append(i)
    i += 1

ultimo_a = todos_a[-1]


total_a = frase.count('a')

primeiro_a = frase.find('a')

print(""" 
A letra A aparece {} vezes nessa frase
Essa mesma letra aparece pela primeira vez na posição {}
E aparece pela última vez na posição {}
""".format(total_a,primeiro_a,ultimo_a))


#Não necessitei de consulta, desenvolvido com facilidade