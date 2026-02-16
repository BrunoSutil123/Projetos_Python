"""
Docstring for jogo_adivinhacao

Projeto: Jogo de Adivinhação
 - Gerar um número aleatório dentro de um intervalo definido.
 - Solicitar palpites do usuário.
 - Informar se o palpite é maior, menor ou correto.
 - Repetir até o usuário acertar.
"""
import os
import random

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


valMax = int(input("Digite o valor máximo para o sorteio de números: "))
numAleatorio = random.randint(1, valMax)
tentativas = 10

while True:
    
    if tentativas > 1:
        chute = int(input(f"Escolha um número entre 1 e {valMax}!! -> "))
        if chute == numAleatorio:
            print(f"PARABENS!!!! você acertou, eu sou o número {numAleatorio}")
            tryAgain = str(input("Deseja tentar novamente? s/n\n->"))
            if tryAgain.lower() == "s":
                tentativas = 10
                limpar_terminal()
                valMax = int(input("Digite o valor máximo para o sorteio de números: "))
                numAleatorio = random.randint(1, valMax)
            else:
                print("saindo...")
                break

        elif chute < numAleatorio:
            tentativas -= 1
            print(f"Quase, o número sorteado é maior que {chute}, tente novamente\n tentativas: {tentativas}\n")
            
        else:
            tentativas -= 1
            print(f"Quase, o número sorteado é menor que {chute}, tente novamente\ntentativas: {tentativas}\n")
            


    else:
        tryAgain = str(input("Acabaram as suas tentativas!!! deseja tentar novamente? s/n\n->"))

        if tryAgain.lower() == "s":
            tentativas = 10
            limpar_terminal()
            valMax = int(input("Digite o valor máximo para o sorteio de números: "))
            numAleatorio = random.randint(1, valMax)
        else:
            print("saindo...")
            break