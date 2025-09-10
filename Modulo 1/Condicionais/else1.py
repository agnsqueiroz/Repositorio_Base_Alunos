# Entrada de dados
idade = int(input("Digite sua idade:"))
estudante = input("É estudante? (s/n): ")

#Lógica para definir preço
if idade <= 12:
    preço = 8.00
elif estudante == "s":
    preço = 12.00
elif idade >= 65:
    preço = 10.00
else:
    preço = 20.00

# Saída
print(f"preço do ingresso: R$ {preço :.2f}")