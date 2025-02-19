import random

numeros = tuple(random.randint(1, 100) for _ in range(5))

for i in numeros:
    print(i, end="  ")
    
print()

print(f"O MAIOR VALOR DENTRO DA TUPLA FOI {max(numeros)}") # metodo max passa o maior valor dentro da tupla
print(f"O MENOR VALOR DENTRO DA TUPLA FOI {min(numeros)}") # metodo min passa o menor valor dentro da tupla
    