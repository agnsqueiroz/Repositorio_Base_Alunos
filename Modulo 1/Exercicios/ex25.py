# Solicita os dados do produto ao usuário
nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto (R$): "))
quantidade = int(input("Digite a quantidade do produto: "))

# Abre (ou cria) o arquivo no modo de adição ('a') e escreve os dados
with open("produtos.txt", "a",) as arquivo:
    arquivo.write(f"Nome: {nome}, Valor: R${valor}, Quantidade: {quantidade}\n")

print("Produto salvo com sucesso no arquivo 'produtos.txt'!")

