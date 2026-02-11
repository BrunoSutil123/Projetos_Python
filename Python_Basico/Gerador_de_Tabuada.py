"""

Projeto: Gerador de Tabuada
 - Solicitar um número ao usuário.
 - Gerar a tabuada desse número (1 a 10).
 - Exibir os resultados de forma organizada.
"""

#Essa função verifica o sistema operacional em que o código está sendo executado. Se for Windows (indicado por 'nt'), ela usa o comando 'cls' para limpar o terminal. Caso contrário, para sistemas Unix/Linux/Mac, ela usa o comando 'clear'.
import os #biblioteca que me permite limpar o terminal

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    Num = int(input("Digite o número que deseja ser feita a tabuada: "))

    NumStart = 0
    print(f"Tabuada do {Num}:\n")

    for NumStar in range(10+1):
        print(f"{Num} * {NumStar} = {Num*NumStar}")
    
    repet = str(input("\nDeseja fazer novamente? s/n\n->"))
    if(repet.lower() == "n"):
        break
    else:
        limpar_terminal()
