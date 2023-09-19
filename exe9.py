#Converter métros em centímetros e milímetros

medida = float(input('\nInforme um número em metros: '))

print(
    '\n{} metro(s) correspondem a {} centimetros e {} milímetros'
    .format(medida, (medida*100), (medida*1000)
    )
)