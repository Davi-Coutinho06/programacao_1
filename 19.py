import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    palpite = 0
    while palpite != numero_secreto:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            if palpite < numero_secreto:
                print("Maior que o número secreto!")
            elif palpite > numero_secreto:
                print("Menor que o número secreto!")
            else:
                print(
                    f"Parabéns! Você acertou! O número secreto era {numero_secreto}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


jogo_adivinhacao()
