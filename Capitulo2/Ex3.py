#Verificar sexo de uma pessoa
sexo = ''
while(sexo!='M' and sexo!='F'):
    if(sexo!=''):
        print('Valor inválido!')
    print('Qual seu sexo?')
    sexo = input('Digite M para masculino e F para feminino: ')

#Mostrar o sexo
if(sexo=='M'):
    print('Você é um homem!')
else:
    print('Você é uma mulher!')    