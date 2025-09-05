import os
os.system ("cls") 

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))


if primeiro_numero == segundo_numero:
    terceiro_numero = primeiro_numero + segundo_numero
else:
    terceiro_numero = primeiro_numero * segundo_numero 

print (f"terceiro_número: {terceiro_numero} ") 