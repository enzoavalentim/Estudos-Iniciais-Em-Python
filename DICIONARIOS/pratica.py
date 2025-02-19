pessoas = {'nome': 'gustavo', 'sexo':'M', 'idade':'22'}
print(f"0 {pessoas['nome']} é {pessoas['sexo']} e tem {pessoas['idade']} anos")

# COLOCANDO DICIONARIOS DENTRO DE LISTAS

brasil = []
uf1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
uf2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(uf1)
brasil.append(uf2)
print(brasil[0]['sigla'])
uf1.copy() # é o metodo de faatimento de dicionarios

estado ={}
br =[]

for c in range(0, 3):
    estado['uf'] = str(input(" DIGITE O NOME DO ESTADO"))
    estado['sigla'] = str(input("DIGITE O A SIGLA DO ESTADO: "))
    brasil.append(estado.copy())
print(brasil)
    