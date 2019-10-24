print("""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirão, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados 
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time chapecoense""")


brasileirao = ("Flamengo", "Santos", "Corinthians", "São Paulo", "Palmeiras", "Internacional", "Atlético-MG", "Bahia",
"Athletico-PR", "Botafogo", "Grêmio", "Fortaleza", "Goiás", "Ceará", "Vasco", "Cruzeiro", 
"Chapecoense", "Fluminense", "CSA", "Avaí")

primeiros5 = brasileirao[0:5]

z4 = brasileirao[-4:]

alfab = sorted(brasileirao)

chape = brasileirao.index('Chapecoense')

print(primeiros5)
print(z4)
print(alfab)
print(chape)