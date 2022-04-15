#Programa que descobre anos bissextos e não bissextos.
ano = int(input('Informe um ano: '))
if ano % 400 == 0 or ano % 4 == 0 and not(ano % 100 == 0):
    print('O ano é bissexto!!!')
else :
        print('O ano não é bissexto ;-;')