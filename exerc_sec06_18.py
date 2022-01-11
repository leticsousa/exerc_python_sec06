n = int(input("Quantos números você quer digitar? "))
maior = 0

for count in range (1, n+1):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
        vezes = 1
    elif numero == maior:
        vezes = vezes + 1

print(f"O maior número digitado foi {maior}.\nO número de vezes que ele foi digitado foi {vezes}.")







