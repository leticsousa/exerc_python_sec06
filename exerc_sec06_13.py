n = (int(input("Digite um número par: ")))

while n % 2 != 0:
    n = (int(input("Este número não é par.\nDigite um número par: ")))

if n % 2 == 0:
    for count in range (0, n+2, 2):
        print(count)
