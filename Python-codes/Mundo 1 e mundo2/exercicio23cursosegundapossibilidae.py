stri = int(input("Informe um valor entre 0 e 9999\n"))
char = str(stri)
nova_strin = char.zfill(4)


u = nova_strin[-1]
d = nova_strin[-2]
c = nova_strin[-3]
m = nova_strin[-4]

print("{} unidades\n{} dezenas\n{} centenas\n{} milhares".format(u, d, c, m))