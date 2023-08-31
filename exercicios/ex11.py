# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$1,00 = R$3,27
valor = float(input('Quantos reais você tem? '))

conversor = valor / 3.27

print('Com esse valor você consegue comprar {} dolares'.format(conversor))