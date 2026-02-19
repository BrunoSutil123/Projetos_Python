"""
Sistema de Cadastro de Usuários
 - Permitir cadastrar múltiplos usuários
 - Armazenar em lista ou dicionário
 - Listar usuários cadastrados
 - Buscar usuário pelo nome
"""
def NewUser(usuarios):
    print("--Cadastro de novos usuarios--")

    while True:
        nome = input("Digite um nome (ou sair): ")

        if nome.lower() == "sair":
            break

        if not nome.strip():
            print("Nome inválido.")
            continue

        try:
            idade = int(input("Digite a idade: "))
        except ValueError:
            print("Idade inválida.")
            continue

        email = input("Digite o email: ")

        newUser = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        usuarios.append(newUser)
        print("Usuário cadastrado com sucesso!\n")


def Lista(usuarios):
    print(f"\nUsuários cadastrados: {len(usuarios)}\n")

    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    for user in usuarios:
        print(f"Nome: {user['nome']}")
        print(f"Idade: {user['idade']}")
        print(f"Email: {user['email']}\n")


def SearchUser(usuarios):
    print("\n--Procurar usuario--")
    search_name = input("Digite o nome do usuario: ")

    for user in usuarios:
        if user["nome"].lower() == search_name.lower():
            print("\nUsuário encontrado:")
            print(f"Nome: {user['nome']}")
            print(f"Idade: {user['idade']}")
            print(f"Email: {user['email']}\n")
            return

    print("Usuário não encontrado.\n")


usuarios = []

while True:
    try:
        menu = int(input(
            "\nPara onde iremos hoje?\n"
            "1) Adicionar novos usuarios\n"
            "2) Lista total de usuarios\n"
            "3) Procurar usuario\n"
            "4) Sair\n-> "
        ))
    except ValueError:
        print("Digite um número válido.")
        continue

    if menu == 1:
        NewUser(usuarios)

    elif menu == 2:
        Lista(usuarios)

    elif menu == 3:
        SearchUser(usuarios)

    elif menu == 4:
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida.")
