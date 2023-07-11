import json

'''
json.dumps(contatos, indent = 4) #Cria um script json do dicionário "contatos", o indent serve para dar o espaçamento de 4 backspace.
json.loads(conteudo) #Pega a estrutura do códgio e transforma ele na estrutura de Python mais apropriadaez dos colchetes, nesse caso.
'''

'''
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

arquivo = open("C:\\Users\\Thiaki\\Documents\\Faculdade\\AulasPython\\Fase03\\Json_Dicionario.json", "w", encoding="UTF-8")
conteudo = (json.dumps(contatos, indent = 4))
arquivo.write(conteudo)
arquivo.close()
'''



arquivo = open("C:\\Users\\Thiaki\\Documents\\Faculdade\\AulasPython\\Fase03\\Json_Dicionario.json", "r", encoding="UTF-8")
conteudo = arquivo.read()
arquivo.close()
agenda = json.loads(conteudo)
print(agenda)