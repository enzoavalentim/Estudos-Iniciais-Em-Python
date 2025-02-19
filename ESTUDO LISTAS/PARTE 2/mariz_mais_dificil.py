matriz = [[], [], [], [], [], [], [], [], []]
pares = list()

def soma_elementos(x):
   soma = 0 
   for i in x:
       soma += i 
       print(soma)

for i in range(0, 9):
    numero = int(input("DIGITE NUMEROS PARA AS POSIÇÕES: "))
    matriz[i].append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)

print(f"[{matriz[0]}] [{matriz[1]}] [{matriz[2]}]")
print(f"[{matriz[3]}] [{matriz[4]}] [{matriz[5]}]")
print(f"[{matriz[6]}] [{matriz[7]}] [{matriz[8]}]")

print("Soma parcial dos elementos pares:")
soma_elementos(pares)
