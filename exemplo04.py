# adicionar conteúdo em arquivo de texto já existente

# abre o arquivo para adicionar informações
arquivo = open('cadastro.txt', 'a')     # a = Append

# cadastra o nome e idade e armazena em um arquivo de texto
while True:
    nome = input('Informe o nome (0 para sair): ')
    if nome == '0':
        break
    idade = int(input('Informe a idade: '))
    arquivo.write(nome + ' - ' + str(idade) + '\n')

arquivo.close()     # fecha o arquivo
