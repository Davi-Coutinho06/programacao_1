def repetir_mensagem(mensagem, numero):
    for i in range(numero):
        print(mensagem)


palavra = input('Digite sua palavra:')
numero2 = int(input('Digite a quantidade de vezes para repetir:'))
repetir_mensagem(palavra, numero2)
