#ler arquivo de texto

#ler arquivo de texto linha por linha 
arquivo = open('nomes.txt', 'r')
nomes = []
#percorrer o arquivo linha por linha 
for linha in arquivo:
    print(linha, end='')
    nomes.append(linha)
print(nomes)
arquivo.close()


#abre arquivo
arquivo = open('nomes.txt', 'r')        # r = read

#copia todo o conteudo do arquivo para uma string
texto = arquivo.read()
print(texto)

#fechar o arquivo
arquivo.close()