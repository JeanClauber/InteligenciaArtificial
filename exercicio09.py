nome = str(input('Nome: '))
sexo = str(input('Sexo: ')).upper()

if sexo == 'MASCULINO':
    print(f'{nome}, é homem.')
elif sexo == 'FEMININO':
    print(f'{nome}, é mulher.')
else:
    print('Digite a opção correta.')