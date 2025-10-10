import os
os.system('cls')

salarioMinimo = float(input("Digite o salario minimo: "))
quilowatts = float(input("digite a quantidade de quilovatts consumida: "))

valor_por_quilovatt = (salarioMinimo/7)/100
valor_a_pagar = quilowatts * valor_por_quilovatt
valor_com_desconto = valor_a_pagar-(valor_a_pagar*0.10)

print(f"Valor por quilowatt: {quilowatts}")
print(f"Valor a ser pago: R${valor_a_pagar}")
print(f"Valor com desconto: R${valor_com_desconto}")