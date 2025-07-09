import random


def sorteio_numero():
    numero_sorteado = random.randint(1, 100)
    return numero_sorteado


numero_aleatorio = sorteio_numero()
print(f'o numero sorteado foi:{numero_aleatorio}')
