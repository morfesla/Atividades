# Recebe dois números inteiros do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula os resultados
soma = num1 + num2
produto = num1 * num2
media = (num1 + num2) / 2

# Verifica menor e maior valor
if num1 < num2:
    menor = num1
    maior = num2
elif num2 < num1:
    menor = num2
    maior = num1
else:
    menor = num1
    maior = num2

# Verifica se são iguais
if num1 == num2:
    iguais = "Os números são iguais"
else:
    iguais = "Os números são diferentes"

# Mostra os resultados (uma linha para cada)
print("Média:", media)
print("Soma:", soma)
print("Produto:", produto)
print("Menor valor:", menor)
print("Maior valor:", maior)
print(iguais)