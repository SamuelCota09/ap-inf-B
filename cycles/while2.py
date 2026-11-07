# Fazer programa que peça números ao utilizador e os some até que seja introduzido 0

n = 1
s = 0

while n != 0:
    n = float(input("Indique um número:"))
    s += n

print("Soma:", s)