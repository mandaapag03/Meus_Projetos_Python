print('Você está em uma floresta escuta, a luz do luar ilimina os itens a sua frente....')
print('--> Itens: PÁ e LANTERNA')
comandos = input('Pegar itens??(y - Yes / n - No): ')
if comandos == 'y':
    print('Você pegou os itens! ')
elif comandos == 'n':
    print('Você não pegou os itens, mas vamos seguir...')   
elif comandos == 'sair':
    comandos = input('Tem certeza que deseja sair?(y - Yes / n - No): ')
    if comandos == 'y':
        print('Fim de jogo!')
else :
    print('REINICIE O JOGO')
