num = 1
soma = 0
media = 0
while num <=10:
    numero = int(input("Digite um número: "))
    num = num + 1
    soma = soma + numero

media = soma/10
print(f"A média dos números digitados é de {round(media, 2)}.")
