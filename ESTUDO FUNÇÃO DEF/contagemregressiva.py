import time
import sys

def linhas():
    print("-="*20)

def contagem(x):
    for i in range(len(x)):
        print(x[i], end="  ")
        sys.stdout.flush()  # Força a exibição imediata da saída
        time.sleep(0.75)
    print()
    
def contagem_reversa(x):
    for i in reversed(range(len(x))):
        print(x[i], end="  ")
        sys.stdout.flush()  # Força a exibição imediata da saída
        time.sleep(0.75)
    print()    
    
def contagem_final(x, y, z):
   
     for i in (range(x, y+1, z)):
        print(i, end="  ")
        sys.stdout.flush()  # Força a exibição imediata da saída
        time.sleep(0.75)
     print()
    
        
        

print("CONTAGEM REGRESSIVA DE 1 ATÉ 10")
linhas()
lst1 = list(range(1, 11))
contagem(lst1)
print("FIM!")
linhas()

print("CONTAGEM REGRESSIVA DE 10 ATÉ 1")
contagem_reversa(lst1)
print("FIM!")

linhas()

print("AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM")
inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))

contagem_final(inicio,fim,passo)
print("FIM!")


