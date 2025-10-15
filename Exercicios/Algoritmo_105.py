import os
os.system('cls')

sigla = input("Digite a sigla da cidade: ")
uf = sigla.upper()

if(uf == "SP"):
    print("Paulista")
elif(uf == "MG"):
    print("Mineiro")
elif(uf == "RJ"):
    print("Carioca")
else:
    print("Outros estados")