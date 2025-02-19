lst = []

x = input("DESEJA ADICIONAR UM VALOR A SUA LISTA [S/N]: ").upper()

while x == "S":
    valor = int(input("DIGITE UM VALOR PARA ADICIONAR À LISTA: "))
    
    if valor in lst:
        print(f"O valor {valor} já está na lista. Não será adicionado novamente.")
    else:
        lst.append(valor)
        print(f"O valor {valor} foi adicionado à lista.")

    x = input("DESEJA ADICIONAR UM VALOR A SUA LISTA [S/N]: ").upper()

print("Lista final:", sorted(lst))
