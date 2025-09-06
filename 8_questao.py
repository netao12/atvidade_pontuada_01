import os 
os.system ("cls") 

print("""
cor  \t\t\t Preço
Verde\t\t\tR$ 10,00
Azul \t\t	R$ 20,00
Amarelo\t\t	R$ 30,00
Vermelho\t	R$ 40,00
""")

cor = str(input("Digite a cor do cd desejado: ")) 

match cor:
    case "verde":
        print("você escolheu o verde, no valor de R$10,00")
    case "azul":
        print("você escolheu o azul, no valor de R$20,00") 
    case "amarelo":
        print("você escolheu o cd amarelo, no valor de R$30,00") 
    case "vermelho": 
        print("você escolheu o cd vermelho, no valor de R$40,00") 
    case _:
        print("Opção inválida") 
    
