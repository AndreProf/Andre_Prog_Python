import os
os.system('cls')

nota_01 = 7
nota_02 = 5
nota_03 = 5
nota_04 = 2

media = (nota_01+nota_02+nota_03+nota_04)/4

if(media >=7):
    print(f"Média {media}, Aluno Aprovado")
elif (media >= 5 and media < 7):
    print(f"Média {media}, Aluno de recuperação")
else:
    print(f"Média {media}, Reprovado")