print('-=' * 15)
print('CAIXA ELETRONICO')
print('-=' * 15)

valor = int(input('Qual valor quer sacar? '))
total = valor 
ced = 50
totaced = 0
while True:
    if total >= ced:
        total -= ced
        totaced += 1
    else:
        if totaced > 0:
            print(f'Total de {totaced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            
            ced = 1
        totaced = 0
        if total == 0:
            break
