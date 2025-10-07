import os
os.system('cls')
# função len() - conta o tamanho da String

texto = "Olá Mundo!"
tamanho = len(texto)

print(f"O tamanho da String {tamanho}")

#Texto todo em letra maiuscula
texto_maiusculo = texto.upper()
print(f"O texto em letra maiuscula '{texto_maiusculo}'")

#Texto com letras minusculas
texto_minusculo = texto_maiusculo.lower()
print(f"O texto em letra minuscula '{texto_minusculo}'")

#Invertendo a posição da String
texto_invertido = texto[::-1]
print(f"String invertida '{texto_invertido}")