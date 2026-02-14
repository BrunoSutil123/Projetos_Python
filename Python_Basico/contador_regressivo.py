"""
Docstring for Contador_Regressivo

Projeto: Contador Regressivo
 - Solicitar um número inicial ao usuário.
 - Realizar uma contagem regressiva até zero.
 - Exibir cada número da contagem.
"""

num = int(input("Digite um numero para decrementar: "))

for num in range(num, 0-1, -1):
    print(num)