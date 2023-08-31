# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
valor = int(input('Digite um valor: '))

centimetros = valor * 100
milimetros = valor * 10000

print('Este valor em centimetros é igual a: {}'.format(centimetros))
print('Este valor em milimetros é igual a: {}'.format(milimetros))