nota = int(           input('digite a nota ')           )
while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10: "))

print(f"Você digitou a nota: {nota}")