#Ler número entre 1000 e 9999
num = 0
while(not(num>=1000 and num<9999)):
    if(num!=0):
        print('Valor inválido!')
    num = int(input('Entre com um número inteiro entre 1000 e 9999: '))

#Mostrar núm da unidade, dezena, centena e milhar
aux = num
print('Unidade = ', aux%10)
aux //= 10
print("Dezena = ", aux%10)
aux //= 10
print("Centena = ", aux%10)
aux //= 10
print("Milhar = ", aux%10)