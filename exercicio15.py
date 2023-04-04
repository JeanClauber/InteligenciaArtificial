import datetime
nome = str(input('Nome: '))
ano_nasc = int(input('Ano nascimento: '))

idade = 2023 - ano_nasc
print(idade)
if idade < 16:
    print(f'{nome}, não é eleitor')
elif idade >= 18 and idade <= 65:
    print(f'{nome}, voto obrigatório.')
elif idade <= 17 or idade >= 66:
    print(f'{nome}, voto facultativo.')