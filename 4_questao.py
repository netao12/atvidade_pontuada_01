import os 
os.system("cls") 


print("""
Fruta\t\t	Até 5 Kg\tAcima de 5 Kg
Morango\t\t	R$ 2,50 por Kg	R$ 2,20 por Kg
Maçã\t\t	R$ 1,80 por Kg	R$ 1,50 por Kg

""") 

cesta = str(input("digite quais frutas você quer adicionar na sua cesta (Morango\Maçã): ")).strip ().lower ()
quilos_morango = int(input("Quantos Kg de morango você deseja?: "))
quilos_maca = int(input("Quantos Kg de maçã você deseja?: ")) 



quilos_morango = quilos_morango * (2.50 if quilos_morango <= 5 else 2.20)
quilos_maca = quilos_maca * (1.80 if quilos_maca <= 5 else 1.50)


valor_total = quilos_morango * 2.50 
valor_com_desconto = valor_total * 10 

valor_total = quilos_maca * 2.80
valor_com_desconto = valor_total * 10 

valor_total = quilos_morango + quilos_maca
quilos_total = quilos_morango + quilos_maca

if valor_total >= 15 or quilos_maca >= 10:
    desconto = valor_total * 0.10
    valor_com_desconto = valor_total - desconto
else:
    desconto = 0
    valor_com_desconto = valor_total

if valor_total >= 15 or quilos_morango>= 10:
    desconto = valor_total * 0.10
    valor_com_desconto = valor_total - desconto
else:
    desconto = 0
    valor_com_desconto = valor_total

print(f"Total a pagar: R$ {valor_com_desconto:.2f}") 
