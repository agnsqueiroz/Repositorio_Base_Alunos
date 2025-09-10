def calcular_media(notas):
    return sum(notas) / len(notas)

def registrar_resultado(nome, media, status):
    with open("resultados_alunos.txt", "a") as arquivo:
        arquivo.write(f"Aluno: {nome} | Média: {media:.2f} | Status: {status}\n")

def main():
    print("=== Sistema de Registro de Alunos ===")

    while True:
        opcao = input("\nDigite 1 para adicionar aluno ou 0 para sair: ")

        if opcao == '0':
            print("Encerrando o sistema. Até logo!")
            break
        elif opcao == '1':
            nome = input("Digite o nome do aluno: ")

            try:
                notas = []
                for i in range(1, 4):
                    nota = float(input(f"Digite a nota {i}: "))
                    if nota < 0 or nota > 10:
                        raise ValueError("A nota deve estar entre 0 e 10.")
                    notas.append(nota)

                media = calcular_media(notas)
                status = "Aprovado" if media >= 7 else "Reprovado"

                registrar_resultado(nome, media, status)
                print(f"{nome} foi {status} com média {media:.2f}.")

            except ValueError as ve:
                print(f"Erro: {ve}")
        else:
            print("Opção inválida! Digite 1 para continuar ou 0 para sair.")

if __name__ == "__main__":
    main()
