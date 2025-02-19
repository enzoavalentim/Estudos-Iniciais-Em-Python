teste =  list()

teste.append("gustavo")
teste.append("18")

galera = list()
galera.append(teste[:])
print(galera)

teste[0] = ("enzo")
teste[1] = (20)

galera.append(teste[:])
print(galera)


print()

teste2 =[[1],[2],[3],[4]]
print(teste2)

for p in teste2:
    print(p)