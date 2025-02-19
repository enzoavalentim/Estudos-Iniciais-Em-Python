lst = list()
lst_impar = list()
lst_par = list()

for valor in range(0,7):
    valor = (int(input("DIGITE 7 VALORES: ")))
    lst.append(valor)
    if valor % 2 == 0:
        lst_par.append(valor)
    else:
        lst_impar.append(valor)
        
        
        
    
print(lst)
print("-="*30)
print("A LISTA COM NUMEROS IMPARES É: ", sorted(lst_impar))
print("A LISTA COM NUMEROS PARES É: ", sorted(lst_par))
