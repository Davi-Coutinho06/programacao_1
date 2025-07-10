def senha_segura(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    if len(senha) < 8:
        return False

    for char in senha:
        if 'A' <= char <= 'Z':
            tem_maiuscula = True
        elif 'a' <= char <= 'z':
            tem_minuscula = True
        elif '0' <= char <= '9':
            tem_numero = True

    return tem_maiuscula and tem_minuscula and tem_numero


minha_senha = input("Digite a senha para verificar: ")
if senha_segura(minha_senha):
    print("A senha é segura.")
else:
    print('A senha não é segura')
