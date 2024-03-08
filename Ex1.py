class ExecaoImpar(Exception):
    pass

try:
    A = int(input("Digite um número inteiro e par:"))
    if A % 2 == 0:
        print("Numero é par")
    else:
        raise ExecaoImpar("O número informado não pode ser impar")
except ExecaoImpar as e:
    print(e)
except ValueError:
    print("Valor informado não é inteiro")