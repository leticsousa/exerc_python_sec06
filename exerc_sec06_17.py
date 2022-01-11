soma = 0

n = (int(input("Digite um número positivo: ")))

while n < 0:
    n = (int(input("Este número não é positivo.\nDigite um número positivo: ")))

if n > 0:
    for count in range (1, n+1):
        soma = soma + count

print(f"A soma dos {n} números naturais é de {soma}.")
