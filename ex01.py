with open('numeros.txt', 'w') as arquivo:
    for i in range(10):
        numero = int(input('Numero: '))
        arquivo.write(f'{numero}\n')
