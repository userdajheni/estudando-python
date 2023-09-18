# Crie um script python que leia dois numeros e tente mostrar a soma entre eles
numA_str = input('Digite um numero: ')
numA = int(numA_str) # força ser inteiro

numB_str = input('Digite outro numero: ')
numB = int(numB_str) # força ser inteiro

soma = numA + numB
print('A soma entre ',numA,' e ',numB,' e igual a ',soma)

# Outra forma de transformar em inteiro é:
# numA = int(input('Digite um numero:'))
# numB = int(input('Digite outro numero:'))
# soma = numA + numB
# print('A soma entre ',numA,' e ',numB,' e igual a ',soma)