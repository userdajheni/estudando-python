n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
mod = n1 % n2
pot = n1 ** n2
divInt = n1 // n2

print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
print('A subtração entre {} e {} é igual a {}'.format(n1, n2, sub))
print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, mult))
print('A divisão entre {} e {} é igual a {}'.format(n1, n2, div))
print('O resto da divisão entre {} e {} é igual a {}'.format(n1, n2, mod))
print('A potencia entre {} e {} é igual a {}'.format(n1, n2, pot))
print('A divisão inteira entre {} e {} é igual a {}'.format(n1, n2, divInt))

# replicar informações
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))