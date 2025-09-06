import os
os.system ("Cls") 

print("""
Combustível	Quantidade Vendida	Desconto por Litro
Álcool\t	Até 25 litros\t\t\t	10%
Álcool\t	Acima de 25 litros\t\t	20%
Gasolina	Até 25 litros\t\t\t	15%
Gasolina	Acima de 25 litros\t\t	30%

""")
preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Digite a quantidade de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()

match combustivel:
    case "A":
        if litros <= 25:
            desconto = 0.10
        else:
            desconto = 0.20
        valor_total = litros * preco_alcool * (1 - desconto)
        print(f"Você escolheu Álcool. Total a pagar: R$ {valor_total:.2f}")

    case "G":
        if litros <= 25:
            desconto = 0.15
        else:
            desconto = 0.30
        valor_total = litros * preco_gasolina * (1 - desconto)
        print(f"Você escolheu Gasolina. Total a pagar: R$ {valor_total:.2f}")

    case _:
        print("Opção inválida. Digite apenas A ou G.")