print("Nota A tem peso 3.5 e a nota B tem peso 7.5")
a = float(input("Digite a nota A: "))
b = float(input("Digite a nota B: "))

notaA = (a * 3.5)
notaB = (b * 7.5)
notaFinal = ( notaA + notaB) / 11

print(f"MEDIA = {notaFinal:,.5f}")
