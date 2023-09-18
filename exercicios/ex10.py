#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
num = int(input('Tabuada do numero: '))
cont = 1

while(cont <= 10):
    print('{} x {} = {}'.format(num, cont, (cont * num)))
    cont = cont + 1