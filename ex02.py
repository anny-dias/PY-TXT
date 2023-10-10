with open('numeros.txt', 'r') as arquivo:
    soma = 0
    for linha in arquivo:
        print(linha, end='')
        soma += int(linha)

    print(f'Somatório: {soma}')

