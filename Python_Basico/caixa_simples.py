"""
Docstring for caixa_simples

Projeto: Simulador de Caixa Eletrônico (Básico)
 - Definir um saldo inicial.
 - Oferecer opções: consultar saldo, sacar e sair.
 - Atualizar o saldo após cada operação.
 - Impedir saques maiores que o saldo disponível.
"""
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


saldo: float = 0.00
escolha = 0

while escolha != 4:
    print("Bem vindo ao caixa eletrônico!\nDigite uma das opções:\n")
    escolha = int(input("1) Consultar saldo\n2) Guardar dinheiro\n3) Sacar\n4) Sair\n-> "))
    limpar_terminal()

    if escolha == 1:
        while True:
            print("-Seu Saldo atual-\n\n")
            print(f"Seu saldo atualmente é de {saldo} Reais.")
            voltar = str(input("Digite 's' para voltar\n-> "))

            if voltar.lower() == "s":
                limpar_terminal()
                break
                
            else:
                limpar_terminal()
                print("Opção inválida!!\n")


    elif escolha == 2:
        while True:
            print("-Guardar dinheiro-\n\n")
    
            try:
                valor = float(input("Digite o valor que deseja guardar\n-> "))
            except ValueError:
                limpar_terminal()
                print("Digite apenas números!\n")
                continue

            if valor <= 0:
                limpar_terminal()
                print("Valor inválido!!\n")
            else:
                saldo += valor
                break

    elif escolha == 3:
        while True:
            print("-Sacar dinheiro-\n\n")
            valor = float(input("Digite o valor que deseja sacar\n-> "))

            if valor < 0 or valor > saldo:
                limpar_terminal()
                print("Valor inválido!!\n")
            else:
                limpar_terminal()
                saldo -= valor
                break

    elif escolha == 4:
        limpar_terminal()
        print("Saindoo....")

    else:
        limpar_terminal()
        print("Valor inválido, digite um valor válido referente as operações bancárias!!\n\n")
        