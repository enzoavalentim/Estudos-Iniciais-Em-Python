lst = []

for cont in range(0,5):
    lst.append(int(input("DIGITE 5 NUMEROS ALEATORIOS: ")))
    
print(lst)
print("-="*30)

print(f"O MAIOR NUMERO DA SUA LISTA FOI {max(lst)}")
print(f"O MENOR NUMERO DA SUA LISTA FOI {min(lst)}")
print("-="*30)


for c, v in enumerate(lst):
    print(f"na posição {c} encontei o valor {v}")