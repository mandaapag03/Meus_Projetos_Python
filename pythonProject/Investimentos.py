valor = float(input('Valor a investir: R$ '))
dias = int(input('Quantidade de dias que deseja investir: '))
opcao = input('Qual investimento? (p - Poupança / c - CDI): ')
selic = float(input('Valor atual da SELIC, em porcentagem: ')) 
if opcao == 'p':
        if selic <= 8.5:
                premio = 0.70 * (selic / 100/12) * valor * (dias//30)
        else:
                premio = 0.005 * (dias//30) * valor
else:
        cdi = selic - 0.1
        premio = valor * (cdi/100/ 360) * dias
        if dias <= 180:
                ir = premio * 0.225
        elif dias <= 360:
                ir = premio * 0.20
        elif dias <= 720:
                ir = premio * 0.175
        else:
                ir = premio * 0.15
        premio -= ir
print(f'Prêmio: R$ {premio:.2f}')
