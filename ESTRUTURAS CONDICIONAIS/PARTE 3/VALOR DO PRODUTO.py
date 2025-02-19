Petiqueta = float(input("INFORME O PREÇO DA ETIQUETA", ))
opcao_pagamento = int(input("INFORME A OPÇÃO DE PAGAMENTO", ))

match opcao_pagamento:
    case 1:
        preco_final = Petiqueta * 0.9
        print("Preço final: ", preco_final)
    case 2:
        preco_final = Petiqueta * 0.95
        print("Preço final: ", preco_final)
    case 3:
        preco_final = Petiqueta
        print("Preço final: ", preco_final)
    case 4:
        preco_final = Petiqueta * 1.1
        print("Preço final: ", preco_final)
    case _:
        print("opção invalida")




