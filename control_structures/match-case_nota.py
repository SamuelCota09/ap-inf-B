# Programa que pede a nota e a diz por extenso

nota = int(input("Indique a nota, entre 1 e 5."))

match nota:
    case 1:
        print("Mau")
    case 2:
        print("Insuficiente.")
    case 3:
        print("Suficiente.")
    case 4:
        print("Bom.")
    case 5:
        print("Muito Bom.")
    case _:
        print("NOTA INVÁLIDA.")   






    
    