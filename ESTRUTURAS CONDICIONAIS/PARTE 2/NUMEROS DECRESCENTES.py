A = int(input("DIGITE O PRIMEIRO NUMERO, "))
B = int(input("DIGITE O SEGUNDO NUMERO, "))
C = int(input("DIGITE O TERCEIRO NUMERO, "))

if A > B and A > C and B > C:
    print(A,B,C)
    
elif A > B and A > C and C > B:
    print(A,C,B)
    
elif B > A and B > C and A > C:
    print(B,A,C)
    
elif B > A and B > C and C > A:
    print(B,C,A)   
    
elif C > B and C > A and A > B:
    print(C,A,B)

elif C > B and C > A and B > A:
    print(C,B,A)