# Ler três valores e mostrá-los por ordem crescente, considere que os 3 inputs são diferentes

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

if n1 < n2 and n2 < n3:
    print(n1, "<", n2, "<", n3)
elif n1 < n2 and n2 > n3:
    if n3 > n1:
        print(n1, "<", n3, "<", n2)
    else:
        print(n3, "<", n1, "<", n2)
elif n1 > n2 and n2 < n3:
    if n1 > n3:
        print(n2, "<", n3, "<", n1)
    else:
        print(n2, "<", n1, "<", n3)

