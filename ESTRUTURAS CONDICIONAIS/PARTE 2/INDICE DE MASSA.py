import math

PESO = float(input("DIGITE O PESO"))
ALTURA = float(input("DIGITE A ALTURA"))

IMC = PESO / (ALTURA * ALTURA) 

if IMC < 18.5:
    print("VOCÊ ESTÁ ABAIXO DO PESO")

elif IMC > 18.5 and IMC < 25.00:
    print("VOCÊ ESTÁ COM PESO IDEAL")
    
elif IMC > 25.00:
    print("VOCÊ ESTÁ ACIMA DO PESO")