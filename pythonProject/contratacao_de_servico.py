#Programa que confirma contrato de um serviço:

nome = (input('Por favor informe seu nome: '))
print('Olá ',nome,', tudo bem?')
pergunta =int(input('Deseja contratar nosso serviço?(1 - yes/0 - no) : '))
#cuidado com o loop do while!!!!
#nao execute o programa
#while pergunta == 0: print('Deseja contratar nosso serviço?(1 - yes/0 - no) : ')
if pergunta == 1 : print('Obrigado por confiar no nosso serviço {0}! Estamos felizes em ter você conosco'.format(nome))
else: print('Então ta bom {0} ;-;'.format(nome))
