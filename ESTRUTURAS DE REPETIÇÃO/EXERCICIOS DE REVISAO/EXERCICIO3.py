import random

numero_aleatorio = random.randint(0, 100)
print("HMMM PENSEI EM UM NUMERO SERA QUE VOCÊ CONSEGUE ADIVINHAR?")
print("\U0001F911") #colocar emoji   https://unicode.org/emoji/charts/full-emoji-list.html
chute = int(input("DIGITE EM QUAL NUMERO ESTOU PENSANDO: "))

while(chute != numero_aleatorio):
    if chute < numero_aleatorio:
        print("ESTOU PENSANDO EM UM NUMERO MAIOR")
        chute = int(input("DIGITE EM QUAL NUMERO ESTOU PENSANDO: "))
        
    elif chute > numero_aleatorio:
        print("ESTOU PENSANDO EM UM NUMERO MENOR")
        chute = int(input("DIGITE EM QUAL NUMERO ESTOU PENSANDO: "))
        
print("PARABENS VOCÊ ACERTOU O NUMERO QUE EU ESTAVA PENSANDO ERA", chute)
    