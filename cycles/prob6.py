"""
Enunciado

Crie um programa que simule um caixa multibanco.

O utilizador começa com um saldo de 1000 €.

O programa deve apresentar repetidamente o seguinte menu:

===== MULTIBANCO =====

1 - Consultar saldo

2 - Depositar dinheiro

3 - Levantar dinheiro

4 - Sair

O utilizador deve escolher uma opção.

Regras:

· Se escolher 1, o programa mostra o saldo atual.

· Se escolher 2, pede o valor a depositar e adiciona esse valor ao saldo.

· Se escolher 3, pede o valor a levantar.

        o Se houver saldo suficiente, o levantamento é efetuado.

        o Caso contrário, deve aparecer a mensagem:

        o Saldo insuficiente!

· Se escolher 4, o programa termina.

· Se introduzir uma opção inválida, deve aparecer a mensagem:

· Opção inválida!

Quando sair, o programa deve mostrar:

Obrigado por utilizar o Multibanco.

–––
"""

import time

saldo = 1000

while True:

    time.sleep(1)
    
    op = int(input("===== MULTIBANCO =====\n 1 - Consultar saldo \n 2 - Depositar dinheiro \n 3 - Levantar dinheiro \n 4 - Sair\n\n"))

    while op < 1 or op > 4:
        print("Opção Inválida! Tente novamente.")
        time.sleep(1)
        
        op = int(input("===== MULTIBANCO =====\n 1 - Consultar saldo \n 2 - Depositar dinheiro \n 3 - Levantar dinheiro \n 4 - Sair\n\n"))

    if op == 1:
        print(f"O Saldo atual é de {saldo} $\n")
    elif op == 2:
        deposito = int(input("Qual é o montante que quer depositar?\n"))
        saldo += deposito
    elif op == 3:
        
        levantamento = int(input("Qual é o montante que deseja levantar?\n"))
        
        while levantamento < 0:
            print("Valor inválido. Tente novamente.\n")
            levantamento = int(input("Qual é o montante que deseja levantar?\n"))

        if levantamento <= saldo:
            print(f"Levantamento de {levantamento} $ efetuado com sucesso.\n")
            saldo -= levantamento
        elif levantamento == -1:
            break
        else:
            print("Saldo insuficiente!\n Tente novamente ou digite -1 para voltar a trás.")
    else:
        break

print("Obrigado por utilizar o Multibanco.")
