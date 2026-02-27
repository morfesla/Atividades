primeira_nota =  float(input("Digite a primeira_nota: "))
segunda_nota = float (input("Digite a segunda_nota: "))

media = (primeira_nota + segunda_nota) /2

if media <7:
    print(f"reprovado: {media}  ")
else:
    print(f"aprovado: {media}")    