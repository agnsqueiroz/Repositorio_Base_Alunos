def cadastrar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    with open("contatos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{telefone},{email}\n")
    print(" Contato salvo com sucesso!\n")


def exibir_contatos():
    print("\n Lista de Contatos:")
    try:
        with open("contatos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("Nenhum contato cadastrado.")
                return
            for linha in linhas:
                nome, telefone, email = linha.strip().split(",")
                print(f"Nome: {nome}, Telefone: {telefone}, E-mail: {email}")
    except FileNotFoundError:
        print("Arquivo de contatos ainda não existe.\n")


def menu():
    while True:
        print("\n--- AGENDA DE CONTATOS ---")
        print("1. Cadastrar novo contato")
        print("2. Exibir contatos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            exibir_contatos()
        elif opcao == "3":
            print("Saindo da agenda. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Executa o menu principal
menu()
