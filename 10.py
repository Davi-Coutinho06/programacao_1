def Maior_numero(num1,num2,num3):
 if num1>=num2 and num1>=num3:
  return num1
 elif num2>=num1 and num2>=num3:
  return num2
 else:
  return num3




lista=[]
for i in range(3):
 numero=int(input(f'Digite seu {i+1} numero:'))
 lista.append(numero)
resultado_maior=Maior_numero(*lista)
print(f'o maior numero é: {resultado_maior}')
