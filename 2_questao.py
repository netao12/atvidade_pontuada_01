import os
os.system("cls") 

nome = input("Digite o seu nome: ").strip()
sexo = input("Digite seu sexo (F para feminino / M para masculino): ").strip().upper()
estado_civil = input("Digite o seu estado civil (Solteira/Casada): ").strip().upper()

anos_de_casada = "Não se aplica"

if sexo == "F" and estado_civil == "CASADA":
    anos_de_casada = input("Quanto tempo casada? (em anos): ").strip()

print("\n======== Dados ========")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil.capitalize()}")
print(f"Anos de casada: {anos_de_casada}")