times = ("Flamengo", "Palmeiras", "Santos", "Grêmio", "Internacional",
    "Fluminense", "Corinthians", "Cruzeiro", "São Paulo", "Vasco da Gama",
    "Botafogo", "Atlético Mineiro", "Bahia", "Sport Recife", "Chapecoense",
    "Fortaleza", "Ceará", "Atlético Paranaense", "Goiás", "Coritiba")

print(times[0:5]) # mostrando os 5 primeiros colocados
print("-="*30)

print(times[16:20]) # ultimos 4 colocados
print("-="*30)

print(sorted(times)) # coloca os times em ordem alfabetica
print("-="*30)

y = (times.index("Chapecoense")) # acha a posição da string dentro da tupla
print(f"A Chapecoense esta na {y}° posição na tabela do campeonato brasileiro")



