# faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor
numero = int(input('Digite um numero: '))

ant = numero - 1
suces = numero + 1

print('O numero digitado foi: {}, seu antecessor é: {} e seu sucessor é: {}'.format(numero, ant, suces))


# versão guanabara
# print('O numero digitado foi: {}, seu antecessor é: {} e seu sucessor é: {}'.format(numero, (numero-1), (numero+1)))