def exibir():
    arquivo = open('nomes.txt', 'r')
    for linha in arquivo:
        print(linha, end='')
    arquivo.close()


def inserir():
    arquivo = open('nomes.txt', 'a')
    nome = input('Digite o nome: ')
    arquivo.write(nome + '\n')
    arquivo.close()
    print('Nome inserido com sucesso.')


def excluir():
    arquivo = open('nomes.txt', 'r')            # abro o arquivo para leitura
    lista = []
    for linha in arquivo:                       # copia os nomes para uma lista
        lista.append(linha.replace('\n', ''))
    arquivo.close()

    nome = input('Informe o nome que será excluído: ')
    if nome in lista:
        lista.remove(nome)                      # remove um nome da lista
        print('Nome excluído com sucesso.')
    else:
        print('Nome não está cadastrado.')

    arquivo = open('nomes.txt', 'w')
    for nome in lista:                          # copia os nomes para o novo arquivo
        arquivo.write(nome + '\n')
    arquivo.close()


while True:
    print()
    print('1 - Exibir')
    print('2 - Inserir')
    print('3 - Excluir')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            exibir()
        case 2:
            inserir()
        case 3:
            excluir()
        case 4:
            break
        case _:
            print('Opção inválida')
