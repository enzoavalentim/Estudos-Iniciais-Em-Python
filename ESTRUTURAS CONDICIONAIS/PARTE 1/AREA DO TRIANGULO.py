import math #importa a biblioteca de operações matematicas

LADO1 = int(input("insira o tamanho do lado 1 do triangulo", )) #define o numero que vai no lado 1
LADO2 = int(input("insira o tamanho do lado 2 do triangulo", )) #define o numero que vai no lado 2
LADO3 = int(input("insira o tamanho do lado 3 do triangulo", )) #define o numero que vai no lado 3

if LADO1 < (LADO2 + LADO3) and LADO2 < (LADO1 + LADO3) and LADO3 < (LADO1 + LADO2): #verifica se os tamanhos dos lados formam um triangulo, para isso verifica se cada lado é menor que a soma dos outros dois
    
    PERIMETRO = LADO1 + LADO2 + LADO3 #soma os lados e calcula o perimetro do triangulo
    AREA = math.sqrt(PERIMETRO * (PERIMETRO - LADO1)*(PERIMETRO - LADO2)*(PERIMETRO - LADO3)) #calcula a area do triangulo
    
    print(AREA) #mostra o valor da area do triangulo 

else:  print("isto não é um triangulo")  
    