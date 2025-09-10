nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

arquivo = open("pessoa.txt", "a")
arquivo.write(nome + "|" + email + "\n")
arquivo.close()