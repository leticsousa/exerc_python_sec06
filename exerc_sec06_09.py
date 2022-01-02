cont = 1
aux = 1

n = (int(input("Digite um número: ")))

while cont <= n:
    aux = aux + 1
    if aux % 2 != 0:
        print(aux)
        cont = cont + 1
