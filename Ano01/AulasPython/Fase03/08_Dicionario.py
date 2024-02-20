'''
dicionario = {
    "Eduardo":"Aluno",
    "Jorge":"Aluno",
    "Matheus":"Professor"
}

dicionario["Eduardo"] #Mostra qual o valor dessa chave
for chaves in dicionario.keys():
    print(chaves) #Exibe todos as chaves separadamente
for valor in dicionario.values():
    print(valor) #Exibe todos os valores separadamente
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}") #Exibe a lista em ordem desempacotamento as tuplas
dicionario["chave"] = "valor" #Adiciona novos itens no dicionario
dicionario.popitem() #Exclui o último item do dicionário
dicionario.pop("Eduardo") #Exclui a chave e o respectivo valor do dicionário
dicionario.clear() #Limpa todos os dados do dicionario
'''

'''
dicionario = {}
escolha = 0

while escolha != 4:
    escolha = int(input("\nDigite sua escola para: \n1 - Adicionar um colaborador e seu cargo \n2 - Remover um colaborador \n3 - Exibir a lista de todos os colaboradores \n4 - Encerrar o programa\n"))
    if escolha == 1:
        nome_colaborador = str(input("Digite o nome do colaborador: "))
        nome_cargo = str(input("Digite o nome do cargo: "))
        dicionario[nome_colaborador] = nome_cargo
    elif escolha == 2:
        remover = str(input("Digite a chave que deseja remover: "))
        dicionario.pop()
    elif escolha == 3:
        for chave, valor in dicionario.items():
            print(f"O colaborador {nome_colaborador} tema funcao de {nome_cargo}")
    elif escolha == 4:
        break
    else:
        print("Opcao invalida, tente novamente")

'''

#DICIONÁRIO COMPOSTO
contatos = {
    "Eduardo":{
        "Celular":"11950868938",
        "E-mail":"thiakiyoshida@gmail.com",
    },
    "Jorge":{
        "Celular":"11098765432",
        "E-mail":"jorge@gmail.com",
    },
}

for nome , telefone_email in contatos.items():
    print(f"o {nome} pode ser contatado por: ")
    for atributo , valor in telefone_email.items():
        print(f"   {atributo} -- {valor}")
    print("")