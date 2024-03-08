class Erro0(Exception):
    pass



try:
    A = int(input("Digite um número inteiro"))
    X = A / 10
    if X != 0:
        print(X)
    else:
        raise Erro0("O número digitado não pode ser zero")
except Erro0 as e:
    print(e)
except ValueError:
    print("Digite apenas números")