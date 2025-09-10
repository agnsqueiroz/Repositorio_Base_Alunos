try:
    # Tentando abrir o arquivo no modo leitura
    with open('meu_arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    # Se o arquivo não existir, ele será criado aqui
    print("Arquivo não encontrado! Criando o arquivo agora...")
    with open('meu_arquivo.txt', 'w') as arquivo:
        arquivo.write("Este é o conteúdo inicial do arquivo.\nCriado automaticamente!")

    # Agora vamos abrir novamente para leitura
    with open('meu_arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo após criação:")
        print(conteudo)
