nome = 'ana'
idade = 18
peso = 85.7
trabalho = True

# print(nome + idade + peso + trabalho) --> isso retorna um erro pois o + concatena apenas string.

# uma das maneiras corretas de concatenar variavel
print(nome, idade, peso, trabalho)

nome_aluno = input('Qual e o seu nome?')
print('O nome digitado foi: ', nome_aluno)

# Crie um script python que leia dois numeros e tente mostrar a soma entre eles
numA = int(input('Digite um numero:'))
numB = int(input('Digite outro numero:'))
soma = numA + numB
print('A soma entre ',numA,' e ',numB,' e igual a ',soma)