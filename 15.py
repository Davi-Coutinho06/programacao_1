def analisa_lista(lista_de_numeros):
    maior = max(lista_de_numeros)
    menor = min(lista_de_numeros)
    media = sum(lista_de_numeros) / len(lista_de_numeros)
    return maior, menor, media


numeros_do_usuario = []
quantidade_numeros = int(
    input("Quantos números você deseja adicionar à lista? "))

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros_do_usuario.append(numero)

if numeros_do_usuario:
    maior_val, menor_val, media_val = analisa_lista(numeros_do_usuario)
    print(f"O maior número é: {maior_val}")
    print(f"O menor número é: {menor_val}")
    print(f"A média dos números é: {media_val}")
else:
    print("A lista está vazia, não é possível analisar.")
