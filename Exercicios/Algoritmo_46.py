import os
os.system('cls')

#forma 1
saldo = float(input("Digite o valor do saldo: "))
novoSaldo = saldo+(saldo*0.25)
print(novoSaldo)

#forma 2
saldo1 = (saldo/100)*1
novoSaldo  = saldo+saldo1
print(novoSaldo)