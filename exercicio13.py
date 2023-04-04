n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é maior')