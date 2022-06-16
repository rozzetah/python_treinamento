# Listas

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
numeros = [1, 3, 5, 7]
letras = ['a', 'b', 'c']

#final = numeros + letras
#print(final)
# Pode ser assim:
numeros.extend(letras)
print(numeros)

cidades [0] = 'Porto Alegre'

# print(cidades)

cidades.append('Santa Catarina') # Adicionando item
cidades.remove('Salvador')
cidades.insert(1, 'Brasília')
cidades.pop(0) #Remover item da lista

print(cidades)