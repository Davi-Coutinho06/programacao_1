def eh_par(numero):
    par = (numero % 2) == 0
    return par


num = float(input('Digite seu numero:'))
resultado = eh_par(num)
if resultado == 1:
    print('True')
else:
    print('False')
