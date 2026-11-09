# Crie um programa que faça uma contagem decresceente de 10 até 0 usando um ciclo. A cada número imppresso, o programa deve aguardar 1 segundo antes de mostrar o próximo.
    # a. time.sleep(1) pausa o programa por 1 s

import time

i = 10

while i >= 0:
    time.sleep(1)
    print(i)
    i -= 1


