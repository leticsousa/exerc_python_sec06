n = int(input("Digite um número inteiro entre 100 e 999: "))

while n < 100 or n > 999:
    n = int(input("Digite um número inteiro entre 100 e 999: "))

for digito in enumerate(n.__str__()):
    print(digito)
