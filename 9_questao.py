import os
os.system("cls")

valor_renda_mensal = float(input("Digite Sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor do emprestimo desejado: ")) 
quantidade_prestacao = int(input("Digite a quantidade da prestação: "))

if valor_emprestimo >= valor_renda_mensal * 10:
    print ("emprestimo concedido") 
else:
    print("Empréstimo negado (valor acima do permitido)")

    valor_prestacao = valor_emprestimo / quantidade_prestacao 


if quantidade_prestacao > valor_renda_mensal * 0.3:
        print(f"Empréstimo negado, o valor da parcela ultrapassa 30% do salário.")
else:
        match quantidade_prestacao:
            case 1:
                print(f"1x de R$ {valor_emprestimo:.2f}") 