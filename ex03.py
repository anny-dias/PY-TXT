
with open('arquivo.txt', 'a') as arquivo:
    
    while True:
        caracter = input('Digite alguma coisa (0 para sair): ')
        if caracter =='0':
            break
        arquivo.write(f'{caracter}\n')



