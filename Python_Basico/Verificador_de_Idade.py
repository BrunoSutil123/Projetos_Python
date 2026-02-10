"""
Docstring for Python_Basico.Verificador_de_Idade

Projeto: Verificador de idade
    - Solicitar a idade do usuário.
    - Classificar a idade em categorias (criança, adolescente, adulto, idoso).
    - Exibir a classificação correspondente.
"""


while True:

    idade = int(input("Digite a sua idade em anos: "))

    if idade < 0:
        print("❌ Valor Inválido!!! digite um valor válido")
    else:
        break

if idade <= 12:
    print(f"Sua idade é: {idade}, você é uma Criança!!")
elif idade > 12 and idade <= 19:
    print(f"Sua idade é: {idade}, você é um adolescente!!")
elif idade > 19 and idade <= 60:
    print(f"Sua idade é: {idade}, você é um Adulto!!")
else:
    print(f"Sua idade é: {idade}, você é um Idoso!!")