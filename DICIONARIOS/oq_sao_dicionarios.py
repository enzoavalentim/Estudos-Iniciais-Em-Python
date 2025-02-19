 # dicionarios servem como listas mas podemos utilizar seus indices como strings

pessoas = {'nome':'pesdro'}
print(pessoas['nome'])

# o append nao funciona nos dicionarios o comando utilizado é mais simples
pessoas['sexo'] = 'M'
print(pessoas)
del pessoas['sexo'] # deleta uma classe dentro do nosso dicionario
print(pessoas)

filme = {'titulo':'satar wars', 'ano':'1977', 'diretor':'george lucas'}
print(filme.values()) # retorna os valores que estao no dicionario nao as classes
print(filme.keys()) # retorna as classes do dicionario
print(filme.items()) # retorna tudo que tem no diciononario
print()
for k, v in filme.items(): # para cada key que cotem os valores dentro do dicionario
    print(f"o {k} é o {v}")
    
# pode-se criar listas com dicionarios dentro