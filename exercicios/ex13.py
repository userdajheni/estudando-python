# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o preço do seu produto: '))
desconto = preco - (preco * (5 / 100))

print('Com 5 porcento de desconto você pagará apenas R$ {}'.format(desconto))