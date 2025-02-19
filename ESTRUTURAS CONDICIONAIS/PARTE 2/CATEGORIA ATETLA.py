IDADE = int(input("Informe a idade do atleta", ))


if(IDADE >= 6 and IDADE <=11):
    print("Infantil")
    
elif (IDADE >= 12 and IDADE <= 17):
    print("Juvenil")

elif (IDADE >= 18):
    print("Profissional")
    
elif (IDADE < 6):
    print("Sem categoria definida")