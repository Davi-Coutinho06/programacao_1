def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado*i
    return resultado


numeros = (int(input('Digite seu numero:')))
print(f'o fatorial é {fatorial(numeros)}')