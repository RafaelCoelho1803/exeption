class Erro(Exception):
    pass
try:
    B = str(input("Digite a primeira frase"))
    A = str(input("Digite a primeira frase"))
    if len(A) != len(B):
        raise Erro("Digite as duas frases do mesmo tamanho sendo apenas letras")
    else:
        print("Está correto")
except Erro as e:
    print(e)