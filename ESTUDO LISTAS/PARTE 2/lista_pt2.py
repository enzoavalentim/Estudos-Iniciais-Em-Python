dados = ["enzo", 25] # lista normal 

pessoas = [["pedro", 25], ["maria", 23], ["joao", 32]] # lista dentro de lista, cada uma esta em um indice da lista pessoas

pessoas.append(dados[:])

print(pessoas[0][0]) # consigo acessar os indices das listas que estão dentro de uma lista principal
print(pessoas[1][1])
print(pessoas[1])