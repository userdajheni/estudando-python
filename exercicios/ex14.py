# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input('Informe o seu salario: '))
novo_salario = salario + (salario * (15 / 100))

print('Com o aumento seu novo salario é de R$ {}'.format(novo_salario))