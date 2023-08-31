# crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um numero: '))
dobro = n1 * 2

print('O dobro deste número é: {}'.format(dobro))

# versão guanabara
num = float(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3
raizqd = num ** (1/2)
print('O dobro valor {}, o triplo vale {} e a raiz quadrada é {:.2f}'.format(dobro, triplo, raizqd))