print('Vamos criar uma tabuada!')

#Entrar com o número e o intervalo da tabuada
num = int(input('De qual número você quer fazer a tabuada? '))
inicial = int(input('Qual o valor inicial do intervalo da tabuada? '))
final = int(input('Qual o valor final do intervalo da tabuada? '))

#Verificar se o intervalo é possível
if(inicial>final):
    print('O intervalo dado não é válido')
else:
    #Calcular e mostrar a tabuada
    print('Tabuada do ', num)
    for i in range(inicial,final+1):
        print(num,'x',i,'=',num*i)