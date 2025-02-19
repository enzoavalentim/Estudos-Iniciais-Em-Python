import random

vetor =[]

for i in range(10):
    vetor.append(random.randint(1,20))

(vetor)

numero = int(input("digite um numero: "))

print()

contador = 0
pos = 0 
while pos < 10:
    if(numero == vetor[pos]):
        contador +=1
        print("numero %d encontrado na posicao %d"(numero, pos))
    