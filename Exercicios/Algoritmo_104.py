import os
os.system('cls')

nome = input("Digite o seu nome: ")
sx = input("digite o seu sexo: ")
idade = int(input("Digite a sua idade: "))

sexo = sx.lower()

if(idade < 25 and sexo == "f"):
    print(f"nome: {nome}\nAceita")
else:
    print(f"nome: {nome}\nNão Aceita")