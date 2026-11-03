# Ler dois valores e mostrá-los por ordem crescente

n1 = input("Insira o primeiro número: ")
n2 = input("Insira o segundo número: ")

if n1 < n2:
    print(n1, "<", n2)
elif n1 > n2:
    print(n2, "<", n1)
else:
    print("Erro")
