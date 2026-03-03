import os

os.system("cls")

#entrada de dados

ano_nascimento = int(input("Digite seu ano de nascimento: "))

matricula = int(input("Digite tua matricula: "))

tempo_de_trabalho = int(input("Digite o tempo de trabalho em anos:"))

# Processamento

idade = 2026 - ano_nascimento

if idade >= 65 or tempo_de_trabalho >= 30:
    resultado = "Requerer Aposentadoria"
else:
    resultado = "Não requerer aposentadoria"


# Saída

print("\n- Resultado -")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo_de_trabalho}")
print(f"Resultado: {resultado}")   