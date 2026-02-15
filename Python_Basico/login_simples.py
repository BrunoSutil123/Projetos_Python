"""
Docstring for login_simples

Projeto: Sistema de Login Simples
 - Definir um usuário e senha fixos no código.
 - Solicitar usuário e senha via teclado.
 - Verificar se os dados informados estão corretos.
 - Exibir mensagem de acesso permitido ou negado.
"""
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


user = "bruno123"
password = 30102005

while True:
    print("--Login--")
    userKey = str(input("Insira o nome de usuario:\n-> "))
    passwordKey = int(input("Insira a senha:\n-> "))

    if userKey == user and passwordKey == password:
        print(f"Bem vindo usuario {user} !!")
        break
    else:
        print("!Login ou senha inválidos! Deseja tentar novamente?")
        chose = str(input("s/n\n->"))
        if chose.lower() == "s":
            limpar_terminal()
        else:
            break
        