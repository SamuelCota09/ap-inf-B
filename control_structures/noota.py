# Programa que pede a nota e a diz por extenso

nota = int(input("Indique a nota, entre 1 e 5."))

if nota == 1:
    print("Mau.")
elif nota == 2:
    print("Insuficiente.")
elif nota == 3:
    print("Suficiente.")
elif nota == 4:
    print("Bom.")
elif nota == 5:
    print("Muito Bom.")
else:
    print("NOTA INVÁLIDA.")