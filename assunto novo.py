import os

os.system("cls")

login = (input("Digite seu login: "))
senha = int(input("Digite tua senha: "))

login_cadastrado = "gabriel"
senha_cadastrada = 123

if login == login_cadastrado and senha == senha_cadastrada:
    print("bem vindo")
else:
    print("Login ou senha inváldos")    