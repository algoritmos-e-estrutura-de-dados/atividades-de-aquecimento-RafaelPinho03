A = int(input("Código da peça 1: "))
B = int(input("Quantidade de peças 1: "))
C = float(input("Valor da peça 1: "))
D = int(input("Código da peça 2: "))
E = int(input("Quantidade de peças 2: "))
F = float(input("Valor da peça 2: "))

print(f"VALOR A PAGAR: R$ {((B * C) + (E * F)):,.2f}")
