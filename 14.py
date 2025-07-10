def numeros_primos(n):
    lista_de_primos = []

    for numero_atual in range(2, n + 1):
        eh_primo_atual = True

        if numero_atual < 2:
            eh_primo_atual = False

        for i in range(2, int(numero_atual**0.5) + 1):
            if numero_atual % i == 0:
                eh_primo_atual = False
                break

        if eh_primo_atual:
            lista_de_primos.append(numero_atual)

    return lista_de_primos


num_limite = int(
    input('Digite um número limite (n) para encontrar os primos: '))

if num_limite < 2:
    print(f"Não há números primos até {num_limite}.")
else:
    primos_encontrados = numeros_primos(num_limite)
    print(f"Os números primos até {num_limite} são: {primos_encontrados}")
