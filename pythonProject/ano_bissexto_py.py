#Programa que descobre anos bissextos e não bissextos.
ano = int(input('Informe um ano: '))
if 400 != 0 and (4 != 0 or (ano % 100 == 0)):
    print('O ano não é bissexto ;-;')
else :
        print('O ano é bissexto!!!')