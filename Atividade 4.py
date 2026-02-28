import os

os.system("cls")

num1 = int(input("digite  o primeiro numero:"))
num2 = int(input("digite o segundo numero: "))

soma = num1 + num2
media = (num1 + num2) /2
produto = num1 * num2

if num1 <num2:
    min = num1
    max = num2
else:
    min = num2
    max = num1

print(f"soma: {soma}\n")
print(f"media: {media}\n")
print(f"produto: {produto}\n")
print(f"min: {min}\n")
print(f"max: {max}\n")