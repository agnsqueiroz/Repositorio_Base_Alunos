lista = [10, 20, 30, 40, 50]

# Passo 1: Adicione 60 no final
lista.append(60)

# Passo 2: Insira 15 na posição 1
lista.insert(1, 15)

# Passo 3: Remova o elemento 30
lista.remove(30)

# Passo 4: Remova o último elemento e guarde em uma variável
ultimo = lista.pop()

# Exibindo resultados
print("Lista final:", lista)        # Saída: [10, 15, 20, 40, 50]
print("Último removido:", ultimo)  # Saída: 60