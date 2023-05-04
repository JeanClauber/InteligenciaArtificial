continuar = True
palavras = [' ']
while continuar:
    palavra = str(input('Digite uma palavra ou frase: ')).upper()
    palavras += palavra
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print(f'A palavra {palavra} é um palindromo.')
    else: 
        print(f'{palavra} não é palindromo.')

    novamente = str(input('Desenha verificar outra palavra? [S/N]')).lower()
    if novamente == 'n':
        continuar = False

print('Programa encerrado.')
