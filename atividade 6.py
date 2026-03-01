# Recebe a idade da pessoa
idade = int(input("Digite sua idade: "))

# Verifica as condições
if idade < 16:
    print("Você não pode votar.")

elif idade >= 16 and idade <= 17:
    print("Seu voto é opcional.")

elif idade >= 18 and idade <= 65:
    print("Seu voto é obrigatório.")

else:  # idade > 65
    print("Seu voto é opcional (não é obrigatório).")