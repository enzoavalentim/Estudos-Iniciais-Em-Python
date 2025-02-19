pessoas = list()
maior = list()
menor = list()

x = input("DESEJA CADASTRAR UMA PESSOA [S/N]: ").upper()

while x == "S":
    dados = list()  # Cria uma nova lista para cada pessoa
    dados.append(str(input("DIGITE O NOME DA PESSOA: ")))
    dados.append(int(input("DIGITE O PESO DA PESSOA: ")))
    pessoas.append(dados[:])  # Adiciona uma cópia dos dados à lista pessoas
    
    if dados[1] >= 100:
        maior.append(dados.copy())  # Adiciona uma cópia dos dados à lista maior
    else:
        menor.append(dados.copy())  # Adiciona uma cópia dos dados à lista menor
    
    x = input("DESEJA CADASTRAR UMA PESSOA [S/N]: ").upper()

print("Pessoas cadastradas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]}")

print()
print("Pessoas com peso maior ou igual a 100:")
for pessoa in maior:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]}")

print()
print("Pessoas com peso menor que 100:")
for pessoa in menor:
    print(f"Nome: {pessoa[0]}, Peso: {pessoa[1]}")



#print(f"O maior peso foi de {max(p_pesados)} ")
#print(f"O menor peso foi de {min(p_pesados)} ")
#print(p_leves)