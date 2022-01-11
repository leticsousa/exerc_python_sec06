n = int(input("Digite um número inteiro: "))
num_par = 0
num_lidos = 0

while n != 1000:
    if n % 2 == 0:
        print(f"O número {n} é par.")
        num_par = num_par + 1

    else:
        print(f"O número {n} não é par.")

    num_lidos = num_lidos + 1
    n = int(input("Digite um número inteiro: "))

print(f"O número de números digitados foi {num_lidos}.\nO número de números pares foi {num_par}.")
