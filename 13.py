def palindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return True
    else:
        return False


pal = input('Digite sua palavra:')
print(palindromo(pal))
