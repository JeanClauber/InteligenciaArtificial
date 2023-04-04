carro = int(input('Velocidade do carro:  '))

if carro > 80:
    multa = 8 * ( carro - 80)
    print('Multado! Você está acima da velocidade permitida.')
    print(f'Sua multa é de R$8,00 reais por km acima de 80km/h e a multa fica R${multa:.2f}')
else:
    print(f'Sua velocidade está ok, dirija com segurança.')