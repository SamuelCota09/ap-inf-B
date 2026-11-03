# Programa que leia o ano atual e o ano de nascimento da pessoa e diga se ela pode ou não  votar nesse ano (não considere dia/mês)

ano_nascimento = input("Em que ano nasceu?")

ano_currente = 2026

idade = (int(ano_currente) - int(ano_nascimento))

if idade >= 18:
    print("Pode votar este ano.")
else:
    print("Não pode votar este ano.")