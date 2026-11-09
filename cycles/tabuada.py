# Peça um número inteiro ao utilizador e exiba a tabuada desse número (de 1 a 10)
"""n = ""
while n not int:"""
n = int(input("Qual tabuada quer?\n"))

i = 1

while i <= 10:
    print(n,"x", i,"=",n*i)
    i += 1