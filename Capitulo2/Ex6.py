import math

#Ler um núm decimal
num = float(input('Entre com um número decimal: '))

#Realizar cálculos com número
print("A raiz quadrada de ", num, " é ", math.sqrt(num))
print("A função teto de ", num, " é ", math.ceil(num))
print("A função chão de ", num, " é ", math.floor(num))
print("A parte inteira de ", num, " é ", math.trunc(num))