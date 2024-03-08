class Maiusculo(Exception):
    pass
try:
    Frase = str(input("Digite apenas letras Maiúsculas:"))
    if Frase.isupper():
        print("Escreveu corretamente")
    else:
        raise Maiusculo("Digite apenas letras Maiúsculas")
except Maiusculo as e:
    print(e)
