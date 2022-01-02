n = (int(input("Digite um número ímpar: ")))

while n % 2 == 0:
    n = (int(input("Este número não é ímpar.\nDigite um número ímpar: ")))

if n % 2 != 0:
    for count in range (n, 0 , -2):
        print(count)
