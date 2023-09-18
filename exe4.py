# Ler dois números inteiros e fazer uma soma, média e produto
num1 = int(input('Informe num1:'))
num2 = int(input('Informe num2:'))
num3 = int(input('Informe num3:'))

# soma
soma = num1 + num2 + num3
produto = num1 * num2 * num3
media = soma / 3


# print(num1, '+', num2, ' = ', total)
print('A soma de {}, {} e {} é {}'.format(num1, num2, num3, soma))
print('O produto de {}, {} e {} é {}'.format(num1, num2, num3, produto))
print('A média de {}, {} e {} é {}'.format(num1, num2, num3,  media))
