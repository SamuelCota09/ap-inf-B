# Calcule o fatorial de um número

f = int(input("Indique um número: \n"))
fat = 1
  
while f > 1:
    fat *= f
    f -= 1

print(fat)

# 6! = 720