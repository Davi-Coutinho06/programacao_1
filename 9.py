def soma_lista(numeros):
    return sum(numeros)


lista = []
quantidade=(int(input('digite a quantidade de numeros:')))
for i in range(quantidade):
    numero = float(input(f'digite o {i+1} numero:1'))
    lista.append(numero)
print(soma_lista(lista))
