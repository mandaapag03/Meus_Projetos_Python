import getpass
print('Cadastre-se na Go Empathy!! ')
email = input('Informe um email para cadastro: ')
password = getpass.getpass('Crie sua senha de 4 números: ')
if not password.isnumeric():
    print('Sua senha deve conter apenas números!!')
    password = input('Crie sua senha de quatro dígitos: ')
else:
    print('Boas vindas a Go Empathy!! Começe a explorar!!')
