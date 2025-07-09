def media(lista_de_numeros):
   soma=sum(lista_de_numeros)
   return soma/len(lista_de_numeros)

numeros_digitados=[]
for i in range(3):
   num= float(input(f'Digite seu {i+1} numero:'))
   numeros_digitados.append(num)

resultado=media(numeros_digitados)
print(f'A media e:{resultado}')

    