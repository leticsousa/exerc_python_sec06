cont = 0
soma = 0

while cont <= 100:
    cont = cont + 1

    if cont % 2 == 0:
        soma = soma + cont

print(f"A soma dos 50 primeiros números pares é de {round(soma, 2)}.")
