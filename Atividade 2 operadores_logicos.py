import os

os.system("cls")

primeira_nota = float(input("Digite a nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota) /2
falta = int(input("Digite a falta:"))

if media <7 or falta >40:
    print("Reprovado")
else:
    print("Aprovado")    
    
print(f"Media: {media}")    

