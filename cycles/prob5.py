"""
5. Jogo da Adivinhação Simples
O que fazer: Gerar um número secreto no código.
Peça ao utilizador ppara tentar adivinhar o número até ele acertar. 
Se ele errar, diga "Número muito baixo ou número muito alto. Tente novamente". 
Se acertar, dê-lhe os parabéns.
"""

import random

numero = random.randint(1, 100)

cont = 1

tentativas = 10
tentativap = tentativas-1

while cont <= tentativas:

    if tentativap == 0:
        print("Perdeste.")
        break
    guess = int(input("Tente adivinhar o número, entre 1 e 100. \n"))
    
    while guess > 100 or guess < 0:
        print("Valor Errado. O número deve estar entre 1 e 100. \n")
        guess = int(input("Tente adivinhar o número, entre 1 e 100. \n"))

    if guess == numero:
        print(
            "Muito Bem!\n O número era", numero, "Acertou o número em ", cont, "tentativas."
            )
        break

    else:
        print(f"Número errado. Restam-lhe {tentativap} tentativas. Tente novamente.")
        
        cont += 1

        if guess > numero:
            print("experimente mais baixo...")

        elif guess < numero:
            print("experimente mais alto...")

    tentativap -= 1
