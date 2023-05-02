from time import sleep

print('-=' * 12)
print('Vamos calcular seu IMC')
print('-=' * 12)

continuar = 's'
cont = totalvalor = 0
valores = []

while continuar == 's':
    while True:
        valor = input("Valor da consulta: ")
        
        if valor.replace(".", "", 1).isdigit():
            # Converte a string em um float
            valor_float = float(valor)
            # Soma o valor pela consulta.
            totalvalor += valor_float
            #armazena os valores recebidos
            valores = valor
            break
        else:
            print("Valor inválido. Digite apenas números!")

    peso = int(input('Digite o seu peso em quilogramas: '))

    altura = float(input('Digite a sua altura em metros: '))

    imc = peso / ( altura ** 2)

    print(f'O seu IMC é: {imc:.2f}')

    if imc <= 18.5:
        print('Abaixo do peso ideal')
    elif imc >= 18.6 and imc <= 24.9:
        print('Você está no peso ideal.')
    else:
        print('Você está acima do peso.')

    continuar = str(input('Desenha verificar outro IMC? [S/N]')).lower()
    cont += 1
    totalvalor += valor_float
    menorValor = min(valor)

print(f'Você consultou {cont} pessoas e o valor ganho foi de R$ {totalvalor}.')

fim = str(input('Gostaria de ver os valores recebidos? [s/n: ' )).lower()

if fim == 's':
    print(f'Os valores recebidos foram: {valores}.')
else: 
    print('Certo, finalizando programa!')
    for i in range (-3, 1):
        sleep(1)
        print(f'{i}')
    print('Encerrado!')
