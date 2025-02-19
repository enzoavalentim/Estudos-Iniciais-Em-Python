numeros =[]
pares = []
impares = []

pos = 0

while (pos < 10):
    valor = int(input()) # digitar numeros até que pos seja = 10
    numeros.append(valor)
    pos += 1
    
for elemento in numeros: # teste pares e impares
    if(elemento % 2 == 0): # se o resto da divisão for 0 o numero é par
        pares.append(elemento)
    else:
        impares.append(elemento) # se não atender o if é impar


print(numeros)
print(pares)
print(impares)