"""
<Pedir um número inteiro positivo ao user (e.g.:4). O programa deve exibir o quadrado desse número em formato de texto usando o caractere *. Se digitar 4, deve aparecer:
****
****
****
****
"""

n = int(input("Indique um número"))

for i in range(n):
    print("*" * n)

# ou
"""
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

"""
