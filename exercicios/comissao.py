A = input("Nome do funcionario: ")
B = float(input("Salário do vendedor: "))
C = float(input("Total vendido no mês: "))
 
comissao = (C * 15) / 100

print(f"Total recebido { comissao + B:,.2f}")
