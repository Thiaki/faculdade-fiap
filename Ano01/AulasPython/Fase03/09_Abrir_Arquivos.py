'''
arquivo.read() #Serve para mostrar o contúdo dentro do arquivo
arquivo.readline() #Exibe uma linha do arquivo de acordo com quantas vezes são utilizadas
arquivo.readlines() #Exibe todas as linhas do aqruivo separadamente pelos \n que são feitos, se transformando em uma lista
arquivo.close() #Sempre fechar o arquivo depois de usar, para que não se torne um arquivo corrompido
arquivo.flush() #Libera o buffer interno
arquivo.seek(coluna,posição) #Controla a posição do cursor no arquivo
arquivo.tell() #Retorna a posição atual do cursor
arquivo.truncate(tamanho) #Redimensiona o arquivo para o tamanho especificado
arquivo.writable() #Retorna o valor "True" se puder escrever no arquivo
arquivo.write("Texto") #Escreve no arquivo "Texto"
arquivo.writelines(lista_string) #Escreve cada elemento de uma lista


with open("{caminho}", "r") as arquivo:
    print(arquivo.read()) #Esse método serve para não precisar fechar o arquivo, e tudo que estiver dentro dele será feito antes do arquivo fechar

'''

arquivo = open("C:\\Users\\Thiaki\\Documents\\Faculdade\\AulasPython\\Fase03\\arquivotxt.txt", encoding="UTF-8")
#encoding serve para mostrar ao python qual é a codificação dele (pode fazer com que caracteres não fiquem errados)

for linhas in arquivo.readlines():
    print(linhas)
arquivo.close()





#Atividade 02
'''
arquivo = open("{caminho do arquivo}", "{manipulação do aquivo a baixo}", encoding="UTF-8") #Mostra o que irá fazendo com esse arquivo
{
#r - Abrir para leitura, default
#w - Abrir para escrita sobrescrevendo o conteúdo
#x - Abrir para criação de arquivo e se já tiver um com o mesmo nome, ele da erro
#a - Abrir para escrita colocando o conteúdo no final sem sobrescrever
#b - Abrir em modo binário
#t - Abrir arquivo em modo de texto
#+ - Abrir para atualização
}
arquivo.write("Hello Word") #Texto para escrever no arquivo
'''

conteudo = "Lorem lorem lorem lorem"
arquivo = open("C:\\Users\\Thiaki\\Documents\\Faculdade\\AulasPython\\Fase03\\arquivotxt02.txt", "w", encoding="UTF-8")

arquivo.write(conteudo)
arquivo.close()