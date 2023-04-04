carro = float(input('Valor do carro na fabrica: R$'))
distribuidor = carro * 0.28
imposto = carro * 0.45
valor_venda = carro + imposto + distribuidor

print(f'O carro com impostos e taxa de distribuição fica R${valor_venda}')