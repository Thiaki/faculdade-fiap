'''
instrumento = ["Violao" , "Baixo" , "Guitarra"] #Cria uma lista
instrumento.append(input("Digite o instrumento que quer acrescentar: ")) #Adiciona um elemento como último
instrumento.insert(0 , input("Digite o instrumento que quer adicionar em primeiro lugar: ")) #Insere um elemento na lista em algum lugar específico
instrumento.pop() #Exclui o último elemento, e se quiser escluir um específico, digite o lugar onde ele se encontra dentro dos parenteses
instrumento.remove("Violao") #Exclui um elemento exato
instrumento.count("Violao") #Conta os elementos
instrumento.reverse() #Inverte os elementos da lista
instrumento.sort() #Ordenando a lista em ordem alfabética ou crescente
tamanho = len(instrumento) # Total de elementos
soma = sum(valores) #Soma dos elementos
print(min(valores)) # Exibe o menor ou maior [min - max] valor de uma lista
for x in instrumentos:
    print(x) #Imprime os valores separados
'''

notas = []
opcao = 0
x = 0
while opcao != 4:
    print("1 - Informar nota \n2 - Digitar uma quantidade limitada de notas \n3 - Exibir notas \n4 - Exibir media")
    opcao = int(input("Digite sua opcao: "))
    if opcao == 1:
        notas.append(float(input("Digite a nota do aluno: ")))
    elif opcao == 2:
        cont = int(input("Digite quantas notas vai informar: "))
        while x != cont:
            notas.append(float(input("Digite a nota do aluno: ")))
            x = x + 1
    elif opcao == 3:
        x = 0
        for x in notas:
            print(x)
        x = 0  
    elif opcao == 4:
        break
    else:
        print("Opcao invalida, tente novamente.")


soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade
print(f"A media das notas é {media:.2f}")