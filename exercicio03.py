cont = 0
escolha = 'S'
while escolha == 'S':
    nome = str(input('Nome do vendedor: '))
    sal_fixo = float(input('Salário fixo: '))
    vendas = float(input('Total vendas: '))

    comissao = vendas * 0.15
    total_sal = comissao + sal_fixo

    print(f'{nome} vendeu {vendas} e o seu salário com comissão será de {total_sal}.')
    cont += 1
    escolha = str(input('Gostaria de calcular outro funcionario? [S;N]')).upper()

    if escolha == 'N':
        break
print(f'Programa finalizado, voce verificou o salario de {cont} vendedores.')
