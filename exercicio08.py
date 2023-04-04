cigarros = int(input('Quantos cigarros fuma por dia: '))
anos = int(input('Quantos anos você fuma: '))

minutos = 10 * (cigarros * anos)
vida_perdida = minutos / 24

print(f'VocÊ fumou {cigarros} por {anos} e perdeu um total de {vida_perdida:.2f} dias')