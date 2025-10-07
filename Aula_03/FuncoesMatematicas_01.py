#Importando a biblioteca matemática
import math
import os
os.system('cls')

#funções básicas
#Raiz quadrada
valor_01 = 9
valor_02 = 3

print(math.sqrt(valor_01))
print(math.sqrt(valor_02))

print("Potencia ou exponenciação")

print(math.pow(2,3))
print(math.pow(valor_01,valor_02))

semMath = 2**3
print(semMath)

print("Arredondar para cima")
print(math.ceil(3.2))
print(math.ceil(-1.8))

print("Arredondando para baixo")

print(math.floor(3.2))
print(math.floor(-1.8))

print("Valor Absoluto")

print(math.fabs(-10))
print(math.fabs(7.5))