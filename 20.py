def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada


lista_a = [1, 2, 3]
lista_b = ["a", "b", "c"]
resultado_intercalado = intercalar_listas(lista_a, lista_b)
print(f"Listas originais: {lista_a}, {lista_b}")
print(f"Lista intercalada: {resultado_intercalado}")

lista_x = [10, 20]
lista_y = ["x", "y"]
print(f"Lista intercalada: {intercalar_listas(lista_x, lista_y)}")
