print("""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é hora de se alistar
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.""")

ano_nasc = int(input("Informe seu ano de nascimento"))
idade = 2019 - ano_nasc
idade_certa = 18

if idade < idade_certa: 
    dif = idade_certa - idade
    print("Faltam {} anos para iniciar seu alistamento!".format(dif))

elif idade > idade_certa:
    dif = idade - idade_certa
    print("Você já passou {} anos da fase de alistamento!".format(dif))

else:
    print("É tempo de se alistar!")