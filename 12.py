def contar_vogais(letras):
    vogais = 'aeiou'
    contador = 0
    for letra in letras:
        if letra in vogais:
           contador= contador + 1
    return contador


palavra_digitada = input('Digite a palavra:')
print(f' existem : {contar_vogais(palavra_digitada)} vogais')
