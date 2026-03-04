print("===== CARDÁPIO =====")
print("1 - Feijoada - R$ 25.00")
print("2 - Lasanha - R$ 20.00")
print("3 - Strogonoff - R$ 18.00")
print("4 - Bife Acebolado - R$ 15.00")
print("5 - Pão com ovo - R$ 5.00")

codigo = int(input("Digite o código do prato desejado: "))

match codigo:
    case 1:
        prato = "Feijoada"
        valor = 25.00
    case 2:
        prato = "Lasanha"
        valor = 20.00
    case 3:
        prato = "Strogonoff"
        valor = 18.00
    case 4:
        prato = "Bife Acebolado"
        valor = 15.00
    case 5:
        prato = "Pão com ovo"
        valor = 5.00
    case _:
        prato = None

if prato:
    print("Prato escolhido:", prato)
    print("Valor: R$", valor)
else:
    print("Código inválido!") 