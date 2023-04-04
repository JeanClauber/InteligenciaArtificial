cont = 0
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper()
    saude = str(input('Estado de saude: [boa/ruim]')).upper()
    cont += 1
    if idade >= 18 and saude == 'BOA':
        print(f'{nome}, está apto para servir.')
    elif idade <= 17 and saude == 'BOA':
        print(f'{nome}, não está apto para servir porque é aindanao completou 18 anos.')
    elif idade >= 18 and saude == 'RUIM':
        print(f'{nome}, não está apto para servir porque a saude está {saude}.')
    elif idade <= 23 and sexo == 'FEMININO':
        print(f'{nome}, não está apta para servir, mulheres so podem se alistar a paritr dis 24 anos.')
    elif idade >= 24 and sexo == 'FEMININO' and saude == 'BOA':
        print(f'{nome}, está apto para o serviço militar.')
    elif idade >= 24 and sexo == 'FEMININO' and saude == 'RUIM':
        print(f'{nome}, tem os requisitos para o serviço, mas saude está ruim. Não apto!')

    continuar = str(input('Quer cadastrar outro aluno? [S/N] ')).upper()
    if continuar == 'N':
        break
print('Fim do programa')
print(f'Você verificou {cont} conscritos.')