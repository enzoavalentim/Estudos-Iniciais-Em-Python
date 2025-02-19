A, B, C = map(float, input ("DIGITE 3 NUMEROS").split())

if A > B and A > C:
    print(A)
    if B > C:
        print(B)
        print(C)
    elif B > C:
        print(C)
        print(B)
        
if B > A and B > C:
    print(B)
    if A > C:
        print(A)
        print(C)
    elif C > A:
        print(C)
        print(A)       

if C > A and C > B:
    print(C)
    if A > B:
        print(A)
        print(B)
    elif B > A:
        print(B)
        print(A) 