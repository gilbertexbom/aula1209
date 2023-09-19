#Ler cinco notas de um estudante e retornar a média

nota1 = float(input('Informe a nota: '))
nota2 = float(input('Informe a nota: '))
nota3 = float(input('Informe a nota: '))
nota4 = float(input('Informe a nota: '))
nota5 = float(input('Informe a nota: '))

print(
    'O estudante obteve \n'
    '{} no 1º Bim \n'
    '{} no 2º Bim \n'
    '{} no 3º Bim \n'
    '{} no 4º Bim \n'
    '{} no 5º Bim \n'
    '\n\n A média é {} '.format(
        nota1,
        nota2,
        nota3,
        nota4,
        nota5,
        ((nota1 + nota2 + nota3 + nota4 + nota5)/5)
    )
)

