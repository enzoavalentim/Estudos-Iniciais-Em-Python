pessoas = list()
dados =list()

for i in range(0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()
    
total_menor = 0
total_maior = 0
    
for p in pessoas:
    
    if p[1] >= 21:
        print(f"O {p[0]} é maior de idade")
        total_maior = total_maior + 1
    else:
        print(f"O {p[0]} é menor de idade")
        total_menor = total_menor + 1
        
    
print(pessoas)
print("-="*30)
print(f"Temos {total_maior} maiores de idade")
print(f"Temos {total_menor} menores de idade")