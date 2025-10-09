import os
os.system('cls')
import math

angulo = float(input("digite o angulo: "))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
secante = 1/cosseno
cosecante = 1/seno
cotangente = 1/tangente

print(seno)
print(cosseno)
print(tangente)
print(secante)
print(cosecante)
print(cotangente)