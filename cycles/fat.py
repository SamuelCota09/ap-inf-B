# Calcule o fatorial de um número

f = int(input("Indique um número: \n"))
ff = f
fat = 1
  
while f > 1:
    fat *= f
    f -= 1

print(ff,"! = ",fat)

# 6! = 720

# Alternativa:

n = int(input("Indique um número: \n"))

cont = 1
f = 1

while cont <= n: # <= !!!
    f *= cont
    cont += 1

print(f)


"""
1.ª:
    -> n = 4; cont = 1; f = 1;
2.ª:

    -> n = 4; cont = 2; f = 1;
3.ª:

    -> n = 4; cont = 3; f = 2;
4.ª:

    -> n = 4; cont = 4; f = 6;

5.ª:

    -> n = 4; cont = 5; f = 24.
"""

# Alternativa 2:
    
n = int(input("Digite um número: "))

fatorial = 1

for i in range(1, n+1):
    fatorial *= i
