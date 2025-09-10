estoque = 50

while True:
    print("\nControle de Estoque")
    print("(1) Adicionar unidades ao estoque")
    print("(2) Remover unidades do estoque")
    print("(3) Verificar estoque atual")
    print("(4) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        quantidade = int(input("Quantas unidades deseja adicionar? "))
        if quantidade > 0:
            estoque += quantidade
            print(f"{quantidade} unidades adicionadas. Estoque atual: {estoque}")
        else:
            print("Por favor, insira uma quantidade válida.")

    elif opcao == '2':
        quantidade = int(input("Quantas unidades deseja remover? "))
        if quantidade > 0:
            if quantidade <= estoque:
                estoque -= quantidade
                print(f"{quantidade} unidades removidas. Estoque atual: {estoque}")
            else:
                print("Erro: não há unidades suficientes no estoque.")
        else:
            print("Por favor, insira uma quantidade válida.")

    elif opcao == '3':
        print(f"Estoque atual: {estoque} unidades")

    elif opcao == '4':
        print("Obrigado por usar nossos serviços!")
        break

    else:
        print("Opção inválida. Tente novamente.")