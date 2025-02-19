import random
from operator import itemgetter

particip = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6),
            'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}

ranking ={}

for k, v in particip.items():
    print(f"{k} tirou {v} no dado")

ranking = sorted(particip.items(), key=itemgetter(1), reverse=True) #intengetter ordenara de acordo com a parte 1 dos itens do dicionario que é a parte de n° do dado
print(ranking)