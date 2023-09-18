# Aluguel de carros: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias o carro foi alugado? '))
km_rodados = float(input('Quantos KM foram rodados? '))

diaria = 60
diaria_km = 0.15

valor = (diaria * dias) + (diaria_km * km_rodados)

print('O preço a ser pago é R$ {}'.format(valor))