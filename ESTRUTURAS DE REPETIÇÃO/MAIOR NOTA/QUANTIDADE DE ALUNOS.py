

maior_nota=0.0
quantidade_candidatos=0

nota = float(input("Informe próxima nota: "  ))
while (nota >= 0.0):
    quantidade_candidatos += 1
    if (nota > maior_nota):
        maior_nota = nota
    nota = float(input("Informe próxima nota: "  ))

print("Quantidade: ", quantidade_candidatos)
print("Maior nota: ", maior_nota)

    
    