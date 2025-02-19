LADOA = int(input("DIGITE O VALOR DO LADO A," ))
LADOB = int(input("DIGITE O VALOR DO LADO B," ))
LADOC = int(input("DIGITE O VALOR DO LADO C," ))

if LADOA < (LADOB + LADOC) and LADOB < (LADOA + LADOC) and LADOC < (LADOA + LADOB):
    
    if LADOA == LADOB == LADOC: 
        print("ESTE É UM TRIANGULO EQUILATERO")
        
    else:
        if LADOA != LADOB and LADOA != LADOC and LADOB != LADOC:
            print("ESTE É UM TRIANGULO ESCALENO")
            
        else:
            print("ESTE É UM TRIANGULO ISÓSCELES")

else:
    print("ISSO NÃO É UM TRIANGULO")