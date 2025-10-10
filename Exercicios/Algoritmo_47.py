import os
os.system('cls')

numero = int(input("Digite um numreo: "))
print(numero)
centena = numero // 100
dezena = (numero%100)//10
unidade = numero % 10
numero_invertido = unidade*100+dezena*10+centena

print(numero_invertido)

num = str(numero)
num_invertido = num[::-1]
num_invertido_int = int(num_invertido)
print(num_invertido_int)
