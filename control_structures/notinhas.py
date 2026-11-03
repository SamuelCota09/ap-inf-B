# Verificar se a nota é insuf, suf, etc.

nota = input("Insira aqui a sua nota: \n")
nota = int(nota)

if  nota < 10:
    print("Insuficiente.")
elif nota < 14:
    print("Suficiente.")
elif nota < 18:
    print("Bom.")
elif nota <= 20:
    print("Muito Bomb")
else:
    print("Valor inválido.")