def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)


frase_digitada = input("Digite uma frase: ")
numero_de_palavras = contar_palavras(frase_digitada)
print(f"A frase tem {numero_de_palavras} palavras.")
