while True:
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é impar')
    
    escolha = str(input('Deseja verificar outro numero? [S/N]')).upper()
    if escolha == 'N':
        break
print('Você encerrou o programa')