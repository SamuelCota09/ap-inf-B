# Ler 10 números e contar os que são pares

cont = 0

for i in range(10):
    n = int(input("Insira um número."))

    if n%2 == 0:
        cont += 1
    else:
        pass

print(cont, "dos números inseridos são pares.")