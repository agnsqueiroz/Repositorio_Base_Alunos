# Solicita ao usuário os números separados por espaço
entrada = input("Digite os números separados por espaço: ")

# Converte a entrada para uma lista de inteiros
numeros = list((int, entrada.split()))

# Inicializa os contadores
positivos = 0
negativos = 0
zeros = 0

# Analisa cada número da lista
for numero in numeros:
    if numero > 0:
        print(f"{numero} é positivo.")
        positivos += 1
    elif numero < 0:
        print(f"{numero} é negativo.")
        negativos += 1
    else:
        print(f"{numero} é zero.")
        zeros += 1

# Exibe o relatório final
print("\nRelatório:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")