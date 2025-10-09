import os
os.system('cls')

#Função que remove os espaços em branco
texto = "    Olá mundo com Python"
print(texto.strip())

#Função replace substitui uma string por outra
texto = "O Python é incrivel!!"
novo_texto = texto.replace("Python","Java")
print(novo_texto)

#função split() divide a string em uma lista com base no delimitador
texto = "Python, Java, C#"
linguagens = texto.split(", ")
print(linguagens)

#função starswith()
texto = "Python é incrivel!!"
print(texto.startswith("Python"))
print(texto.startswith("Java"))