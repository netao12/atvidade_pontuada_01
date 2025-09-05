import os
os.system("cls") 


nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite seu sexo: (feminino or masculino): ")).strip ().lower ()
estado_civil = str(input("Digite o seu estado civil:(Solteira/Casada): ")).strip ().lower()

anos_de_casada = "não se aplica"
    
if sexo == "feminino" and "estado_civil" == "casada": 
    anos_de_casada =(input("Quanto tempo casada? (em anos): ")) 


print("\n======== Dados ========")
print(f"Nome: {nome}")
print(f"Sexo: {sexo.capitalize()}")
print(f"Estado Civil: {estado_civil.capitalize()}")
print(f"Anos de casada: {anos_de_casada}")