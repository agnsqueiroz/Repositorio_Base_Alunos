# Lista inicial 
nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial:", nomes)

#Adicionando elementos 
nomes.append("Carlos") #Adiciona ao final
print("Após append:", nomes)

nomes.insert(1, "Fernanda") #Insere "Fernanda" na posição 1
print("Após insert:", nomes)

#Modificando Elementos
nomes[2] = "Paulo" #Modifica o elemento no índice 2
print("Após modificação:", nomes)



#Removendo elementos 
del nomes [3] #Remove o elemento do índice 3
print("Após del:", nomes)

nomes.remove("Maria") # Remove a primeira ocorreência de "Maria"
print("Após remove", nomes)

removido = nomes.pop(2) #Remove e retorna o elemnto da índice 2
print(f"Após pop(removido'{removido}'):", nomes)

nomes.clear() #Esvazia a lista
print("Após clear:", nomes)