import os

os.system("cls")

nota = float(input("Digite a nota: "))

if 0 <= nota <=10:
    print(f"{nota}")
else:
    print("a nota tem que está entre 0 e 10")      

