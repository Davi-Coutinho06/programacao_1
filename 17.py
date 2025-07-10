import random


def simular_dado(n):
    resultados = []
    for _ in range(n):
        resultados.append(random.randint(1, 6))
    return resultados


numero_rolagens = int(input("Quantas vezes você quer rolar o dado? "))
simulacao = simular_dado(numero_rolagens)
print(f"Resultados das rolagens: {simulacao}")
