def contador(* x): # qualquer numero de parametros
    for valor in x:   # para cada valor armazenado na variavel x mostre um por um
        print(valor, end="") # o end faz nao quebrar linha
    print()
    tamanho = len(x) # calcula o tamanho da tupla que chamamos pelo contador
    print(tamanho)
    
contador(1,2,3,4,5)
