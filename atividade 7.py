# Solicita dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Mostra os números informados
print("Primeiro número:", num1)
print("Segundo número:", num2)

# Verifica qual é o maior e o menor
if num1 > num2:
    maior = num1
    menor = num2
elif num2 > num1:
    maior = num2
    menor = num1
else:
    maior = num1
    menor = num2

# Mostra os resultados
print("Maior número:", maior)
print("Menor número:", menor)