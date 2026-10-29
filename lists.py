notas = [15, 18, 12, 17, 14]

# Mostrar a lista completa

print(notas)

# Mostrar a primeira nota

print(notas[0])

# Mostrar a última nota

print(notas[4]) # ou print(notas[-1])

soma = 0

for i in notas:
    soma = soma + i

# ou sum(notas)

media = soma/len(notas)

print("média= ", media)