print('Vamos calcular o preço de sua passagem!')

#Ler distância da viagem
dist = float(input('Qual a distância da sua viagem, em km? '))

#Calcular e mostrar preço da passagem
if(dist<=200):
    preco = dist*0.5
else:
    preco = dist*0.45

print('O preço da viagem é R$%.2f' %preco)