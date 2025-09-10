saldo = 1000.0  # saldo inicial

while True:
    print("\nCaixa Eletrônico")
    print("(1) Sacar")
    print("(2) Depositar")
    print("(3) Ver Saldo")
    print("(4) Sair")
    option = int(input("Opção: "))

    if option == 1:
        valor_sacar = float(input("Valor para sacar: "))
        if valor_sacar <= saldo:
            saldo -= valor_sacar
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para esse saque.")
    elif option == 2:
        valor_depositar = float(input("Valor para depositar: "))
        if valor_depositar > 0:
            saldo += valor_depositar
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    elif option == 3:
        print(f"Seu saldo é R$ {saldo:.2f}")
    elif option == 4:
        print("Obrigado por usar o caixa eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")