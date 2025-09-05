import os 
os.system("cls") 

segunda_nota= float(input("Digite a primeira nota "))
primeira_nota= float(input("Digite a segunda nota "))


media = (primeira_nota + segunda_nota) / 2

if media >= 6: 
    print ("Parabéns")

elif media >= 4.1 and media <= 5.9: 
    print ("Recuperação")

elif media <= 4: 
    print ("Reprovado")
    
print(f"Média: {media}") 
