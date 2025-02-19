investimento = float(input("DIGITE O INVESTIMENTO MENSAL: "))
tx_mensal =  float(input("COLOQUE A PORCENTAGEM EM NUMEROS DECIMAIS: "))
tx_mensal += 1.0 
montante = 0
meses = 0


while(montante < 1000000):
    montante += investimento 
    montante = montante * tx_mensal
    meses += 1

anos = meses // 12
nmeses = meses % 12
print("VOCE ATINGIRA R$ 1.000.00,00 EM", anos, "ANOS E", nmeses, "MESES")

    
    
    
    
    
    