values = []

for i in range(5):
    values.append(i)

print(values)

"""
range(5) -> [0,1,2,3,4]

range(2,8) -> [2,3,4,5,6,7]

range(2,10,2) -> [2,4,6,8]
"""
n = int(input())

soma = 0

for i in range(n):
    num = int(input())
    soma += num

media = soma/n

print(media)


