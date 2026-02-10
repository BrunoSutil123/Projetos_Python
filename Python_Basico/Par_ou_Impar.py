"""
Docstring for Python_Basico.Calculadora_Simples

Projeto: Par ou ímpar
- fazer um projeto onde seja possível fazer a coleta de um número, digitado pelo usuário, e após isso, seja retornado a resposta ímpar ou par de acordo com o número armazenado.
"""

print("Seja bem vindo ao programa Par ou Ímpar!!")
numero = int(input("Digite um número: "))

if numero %2 == 0:
    print(f"O número {numero} é Par!!")
else:
    print(f"O número {numero} é Ímpar!!")