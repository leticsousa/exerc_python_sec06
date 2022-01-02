num = 1
maior = 0
menor = 0

while num <=10:
    numero = int(input("Digite um número: "))
    num = num + 1
    if numero > maior:
        maior = numero
    else:
        menor = numero

print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")
