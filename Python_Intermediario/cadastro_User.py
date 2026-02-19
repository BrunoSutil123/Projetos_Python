"""
Sistema de Cadastro de Usuários
 - Permitir cadastrar múltiplos usuários
 - Armazenar em lista ou dicionário
 - Listar usuários cadastrados
 - Buscar usuário pelo nome
"""

usearios = []

while True:

    nome = str(input("Digite um nome (ou sair): "))

    while not nome.strip():
        print("Nome inválido. Por favor, digite um nome válido.")
        nome = str(input("Digite um nome (ou sair): "))


    if nome.lower() == 'sair':
        break

    idade = int(input("Digite a idade: "))
    email = str(input("Digite o email: "))
    
    
    newUser = {
        "nome": nome,
        "idade": idade,
        "email": email
    }


    usearios.append(newUser)

print(f"\nUsuários cadastrados: {len(usearios)}\n")
for user in usearios:
    print(f"Nome: {user['nome']}\nIdade: {user['idade']}\nEmail: {user['email']}\n")
