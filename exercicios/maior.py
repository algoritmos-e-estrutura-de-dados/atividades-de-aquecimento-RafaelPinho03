from ast import If


A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))
C = int(input("Digite o último número: "))

maiorAB = ((A + B + abs(A - B)) / 2)

print(f"{(maiorAB + C + abs (maiorAB - C )) /2} é o maior")
