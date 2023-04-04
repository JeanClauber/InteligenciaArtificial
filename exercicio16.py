nome = str(input('Nome funcionario: '))
salario_atual = int(input(f'Qual o salário atual de, {nome}: R$'))
salario_min = 1320
restante = salario_atual / salario_min

if restante <= 2:
    novo_salario = salario_atual + (salario_atual * 0.50)
    print(f'O novo salário de {nome} será R${novo_salario}.')
elif restante >= 3 and restante <= 10:
    novo_salario = salario_atual + (salario_atual * 0.20)
    print(f'O novo salário de {nome} será R${novo_salario}')
else:
    novo_salario = salario_atual + (salario_atual * 0.15)
    print(f'O novo saláro de {nome} será de R${novo_salario}')
    