nome = str(input('Nome: '))
valor_hora = float(input('Quanto ganha por hora: R$ '))
horas = int(input('Horas trabalhadas por dia: '))
dias = int(input('Quantos dias uteis teve no mes: '))

escolha = str(input('Você fez horas extras este mes: [S/N]')).upper()
while escolha is not 'SN':
    if escolha == 'N':
        salario = dias * (valor_hora * horas)

        print(f'Olá {nome}, você trabalha {horas} este mês e vai receber um total de {salario}')
        break
    else:
        h_extras = int(input('Quantas horas extras foram feitas: '))
        valorExtra = h_extras * valor_hora
        salario = h_extras + (dias * (valor_hora * horas))
        print(f'Olá {nome}, seu salário com horas extras fica {salario}')
        break
print('Fim do programa')