# Lista de compras
lista_compras = ["arroz", "feijao", "quiabo"]

# Imprime a lista de compras inicial
print("Lista de compras inicial:", lista_compras)

# Remove o elemento "feijao" da lista usando o método pop()
lista_compras.pop(1)

# Imprime a lista de compras após remover "feijao"
print("Lista de compras após remover 'feijao':", lista_compras)

# Adiciona novamente o "feijao" na lista
lista_compras.append("feijao")

# Imprime a lista de compras após adicionar "feijao" novamente
print("Lista de compras após adicionar 'feijao' novamente:", lista_compras)

# Retorna o índice do elemento "arroz" na lista usando o método index()
indice_arroz = lista_compras.index("arroz")
print("Índice do 'arroz' na lista:", indice_arroz)

# Retorna a quantidade de vezes que "feijao" aparece na lista usando o método count()
quantidade_feijao = lista_compras.count("feijao")
print("Quantidade de 'feijao' na lista:", quantidade_feijao)

# Ordena a lista em ordem alfabética usando o método sort()
lista_compras.sort()

# Imprime a lista de compras ordenada
print("Lista de compras ordenada:", lista_compras)

# Inverte a ordem da lista usando o método reverse()
lista_compras.reverse()

# Imprime a lista de compras invertida
print("Lista de compras invertida:", lista_compras)
