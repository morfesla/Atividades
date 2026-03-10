# Ler peso e altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcular IMC
imc = peso / (altura * altura)

# Mostrar IMC
print("Seu IMC é:", round(imc, 2))

# Classificação
if imc < 18.5:
    print("Classificação: abaixo do peso")

elif imc <= 24.9:
    print("Classificação: peso ideal")

elif imc <= 29.9:
    print("Classificação: levemente acima do peso")

elif imc <= 34.9:
    print("Classificação: obesidade grau I")

elif imc <= 39.9:
    print("Classificação: obesidade grau II (severa)")

else:
    print("Classificação: obesidade grau III (mórbida)")