#Ler nome completo
nome = input('Qual seu nome completo? ')

#Mostrar nome com todas as letras maiúsculas
print(nome.upper())

#Mostrar nome com todas as letras minúsculas
print(nome.lower())

#Mostrar quantas letras ao todo tem o nome
print('Seu nome tem ', len(nome)-nome.count(' '), ' letras') #qtd caracteres menos qtd espaços

#Mostrar com o último nome "do Inatel"
ultimo = nome.split()[-1]
print(nome.replace(ultimo, "do Inatel"))
