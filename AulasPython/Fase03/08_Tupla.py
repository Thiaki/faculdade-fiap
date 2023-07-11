'''
#Tuplas
tupla = (2 , 54 , 32)

tupla.count(2) #Conta quantos elementos tem na tupla
tupla.index(32) #Mostra qual o número do elemento na tupla 
min(tupla) #Mostra o menor número da tupla
max(tupla) #Mostra o maior número da tupla
sum(tupla) #Mostra a soma de todos os números da tupla
len(tupla) #Mostra a quantidade de elementos de uma tupla
tuple(tupla) #Converte o objeto em uma tupla
for cont, numero in enumerate(tupla):
    print(f"No índice {cont} temos: {numero}") #Mostra os indices e deus respectivos valores
any(tupla) #Mostrará False se todos os elementos forem 0 ou se estiverem vazio, se tiverem algum valor, retornará 1
all(tupla) #Retorna True se o resultado final tiver True ou se estiver zerado, se não retornará False
'''

tupla = ("João" , "Maria" , "Jorge")
#Desempacotamento da tupla, onde associa cada elemento da tupla para cada variável
teste1 , teste2 , teste3 = tupla
print(teste1)
print(teste2)
print(teste3)

#Exibir os valores separadamente igual a lista
for tupla in tupla:
    print(tupla)
    