# tuplas são variaveis compostas, em que podemos adicionar mais de um valor a variavel
# depois podemos chamar cada valor dessse individualmente, lembrando que os indices começam do zero

x = ("lanche","suco", "pizza", "pudim")

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[0:2]) # fatiamento mostar os indices até o 2 mas exclui o 2
print(x[1:]) # o 1: serve para o print começar do 1 e ir até o final da tupla
print(x[-1]) # da pra varrer ao contrario tbm

print(len(x)) # len mostra o comprimento da tupla
print()
    
# TUPLAS SÃO IMUTAVEIS, EX NAO TEMOS COMO TIRAR O PUDIM DA TUPLA 

for c in x: # para cada "c" (c é cada string dentro de x) na variavel x
    print(c)

for cont in range(len(x)):                     # temos 3 soluções para varrer uma tupla
    print(x[cont])
    
for pos, comida in enumerate(x):
    print(f"Eu cou comer {comida} na posição {pos}")
    
print(sorted(x)) # ORGANIZA AS STRINGS DE X EM ORDEM ALFABETICA


y = (1,2,3,4,5,6,5)
print(y.count(5)) # quantas vezes o numero 5 aparece dentro da tupla y
print(y.index(5)) # em que poseição esta o 5 na tupla y
