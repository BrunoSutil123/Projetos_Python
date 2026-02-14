"""
Docstring for Conversor_de_Medidas

Projeto: Conversor de Medidas
 - Solicitar um valor numérico ao usuário.
 -  Oferecer opções de conversão (ex: km → m, m → cm, °C → °F).
 - Realizar a conversão conforme a escolha.
 - Exibir o resultado convertido.

"""

val = float(input("Digite um valor numérico para a conversão: "))

while True:

    option = int(input("Escolha uma das opções abaixo:\n1)Km->m\n2)m->cm\n3)°C->°F\n-> "))

    if option == 1:
        print("\nConvertendo...")
        valConvertido = val * 1000
        print(f"A conversão de {val}Km para m = {valConvertido}m")
        break

    elif option == 2:
        print("\nConvertendo...")
        valConvertido = val * 100
        print(f"A conversão de {val}m para cm = {valConvertido}cm")
        break

    elif option == 3:
        print("\nConvertendo...")
        valConvertido = val * 9/5+32
        print(f"A conversão de {val}°C para °F = {valConvertido}°F")
        break

    else:
        print("Valor inválido!!! Tente novamente...\n\n")

