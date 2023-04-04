print('-=' * 15)
print('Mercado baratão')
print('-=' * 15)

lista = []
continuar = 'S'
cont = total_produtos = 0

while continuar is not 'N':
    produto = str(input('Produto: '))
    lista.append(produto)
    preço = float(input(f'Valor do {produto}: R$'))
    cont += 1
    total_produtos += preço
    continuar = str(input('Registrar mais produtos? [S/N]')).upper()

    if continuar == 'N':
        
        break

print(f'Você vai comprar {lista}')
print(f'O valor total é R${total_produtos:.2f}.')

print('Qual a forma de pagamento? ')
print('Debito, Credito, DInheiro')
forma = str(input(' ')).upper()

if forma == 'DEBITO' or forma == 'CREDITO':
    print(f'Pagamento de {total_produtos:.2f} no {forma} feito com sucesso!')
elif forma == 'DINHEIRO':
    valor_dinheiro = float(input('Quanto vai pagar no dinheiro: R$ '))
    if valor_dinheiro > total_produtos:
        troco = valor_dinheiro - total_produtos
        print(f'Pagamento de {total_produtos} pago com sucesso, seu troco é de {troco:.2f}')
    elif valor_dinheiro < total_produtos:
        print(f'O valor é insuficiente para efetuar a compra, gostaria de mudar a forma de pagamento?')
        forma = str(input('Forma de pagamento ou cancelar compras: ')).upper()
        if forma == 'CANCELAR':
            print('cancelado')
if forma == 'CANCELAR':
    print('Você cancelou as compras, obrigado e esperamos que volte sempre!')
else:
    print('Muito obrigado por comprar conosco')

continuar = str(input('Registrar novas compras? [S/N]')).upper()