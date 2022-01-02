n = (int(input("Digite um número par: ")))

while n % 2 != 0:
    n = (int(input("Este número não é par.\nDigite um número par: ")))

if n % 2 == 0:
    for count in range (n, -1, -2):
        print(count)
