cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    x = int(input("DIGITE UM NUMERO ENTRE 0 E 20: "))
    if x <= 20:
        print(cont[x])
        break
    else:
        print("O NUMERO DIGITADO NAO ESTÁ ENTRE 0 E 20")