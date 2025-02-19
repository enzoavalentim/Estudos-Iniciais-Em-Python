A, B = map(int, input ("DIGITE 2 NUMEROS, ").split())
operacao_aritmetica = input("DIGITE QUAL TIPO DE OPEÇÃO DESEJA FAZER, ")

match operacao_aritmetica:
    case "SOMA":
       print(A + B) 
    case "SUB":
       print(A - B) 
    case "DIV":
       print(A // B) 
    case "MULT":
       print(A * B) 
    case _:
        print("OPERAÇÃO INVALIDA")  
    
    
