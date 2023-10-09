lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
lista_produtos.insert(8, 'base')
lista_produtos.insert(9, 'corretivo')

print(lista_produtos)

for produtos in lista_produtos :
    print("Temos " + produtos + " à venda!")