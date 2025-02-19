valores = list()

for cont in range(0,5):
    valores.append(int(input("DIGITE CINCO VALORES PARA A LISTA: ")))

for c, v in enumerate(valores):
    print(f"na posição {c} encontei o valor {v}")
print(valores)

copy_valores = valores[:] # copy_valores não tem ligação com valores, com essa função ele copia apenas o conteudo de valores
