print('Você está em uma floresta escura, a luz do luar ilumina os itens a sua frente....')
print('--> Itens: PÁ e LANTERNA')
comandos = input('Pegar itens??(y - Yes / n - No): ')
comandos.lower()
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
    
print('='*100)
print('Você tem dois caminhos, um ao NORTE e o outro a LESTE...')
comandos = input('NORTE ou LESTE?')
comandos.lower()
if comandos == 'NORTE':
    print('Você foi para o norte')
elif comandos == 'LESTE':
    print('Você foi para o leste')



