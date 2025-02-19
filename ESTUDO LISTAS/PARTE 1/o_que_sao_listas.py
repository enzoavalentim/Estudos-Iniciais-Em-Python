# listas são bem parecidas com tuplas, mas listas podem ser mutaveis e escrevos elas entre chaves []

lista = [1,2,3,4,5,6]
print(lista)
print("-="*30)

lista.append(7) # adiciona um elemneto no final da lista
print(lista)
print("-="*30)

lista.insert(0,0) # adiciona o elemento 0 na posição 0 da nossa lista
print(lista) # o insert tambem joga todos elementos uma posição para frente de acordo com a posição passada com parametro

# maneiras de eliminar elementos
del lista[3] # deleta o elemento de acordo com a posição passada entre chaves
lista.pop(3) # deleta o elemento de acordo com a posição passada entre chaves
lista.remove("1") # no metodo remove nao indicamos o indice e sim o valor que queremos tirar da lista
# em todas essas maneiras de eliminar o python reorganiza a lista de acordo com as posições excluidas 

# verificando se o elemento esta na lista

if "1" in lista:
    lista.remove("1")
    
# criando listas com range
x = list(range(0, 11)) # cria uma lista de 0 a 10 
x.sort() # comando ordena os valores do menor para o maior
x.sort(reversed=True) # comando ordena os valores do maior para o menor
len(x) # conta quando elementos temos na lista começando de 0