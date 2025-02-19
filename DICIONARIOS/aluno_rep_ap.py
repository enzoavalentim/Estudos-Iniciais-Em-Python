aluno ={}

aluno['nome'] = str(input("DIGITE O NOME DO ALUNO: "))
aluno['media'] = float(input("DIGITE A MEDIA DO ALUNO: "))

print(f"O NOME É IGUAL A {aluno['nome']}")
print(f"A MEDIA É IGUAL A {aluno['media']}")
if aluno['media'] >= 6:
    print("SITUAÇÃO É IGUAL A APROVADO")
else:
    print("A SITUAÇÃO É IGUAL A REPROVADO")