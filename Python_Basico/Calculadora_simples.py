"""
Docstring for Calculadora_simples

Projeto: Calculadora Simples
 - Solicitar dois números ao usuário.
 - Solicitar a operação desejada (soma, subtração, multiplicação ou divisão).
 - Realizar o cálculo de acordo com a opção escolhida.
 - Exibir o resultado final.
 - tratar erro de divisão por zero.
"""

print("Seja bem vindo a Calculadora!!")

while True:

    N1 = float(input("Digite o primeiro número: "))
    N2 = float(input("Digite o segundo número: "))
    
    while True:
        Operacao = str(input("Digite qual operação deseja fazer:\n-Soma\n-Subtração\n-Multiplicação\n-Divisão\n-> "))

        if(Operacao.lower() == "soma"):
            print(f"{N1} + {N2} = {N1 + N2}\n")
            break

        elif(Operacao.lower() == "subtração" or Operacao.lower() == "subtracao"):
            print(f"{N1} - {N2} = {N1 - N2}\n")
            break

        elif(Operacao.lower() == "multiplicação" or Operacao.lower() == "multiplicacao"):
            print(f"{N1} * {N2} = {N1 * N2}\n")
            break

        elif(Operacao.lower() == "divisão" or Operacao.lower() == "divisao"):
            if(N2 == 0):
                print("!!ERROR!! Não é possível multiplicar por zero!!")
                break
            else:
                print(f"{N1} / {N2} = {N1 / N2}\n")
                break

        else:
            print("Operação Não encontrada!! tente novamente")

    escolha = str(input("\nDeseja tentar novamente? s/n\n-> "))
    if(escolha.lower() == "s"):
        print("\n\n")
    else:
        print("Calculadora desligando.... Até mais!")
        break