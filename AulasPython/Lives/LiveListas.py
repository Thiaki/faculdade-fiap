#https://drive.google.com/drive/folders/1k5ZuWWPq9JE7JOL5yl_AcVjGR0DvLxfh
'''
#EXERCÍCIO 05
#A idéia é representar cada carta como uma string de 2 letras:
#    as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
#    os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
    
#O J de ouros, por exemplo, é representado pela string 'Jo'. O ás de copas, pela string 'Ac'

#esreva um código que recebe um naipe de cartas ('o', que significa ouros, 'p', que significa paus, 'c' de copas ou 'e' de espadas) e produz uma lista com todas as cartas desse naipe.

#Entao, se você receber 'c', deve retornar deve exibir uma lista com 13 cartas, o ás de copas representado pela string 'Ac', os números '2c','3c',...'10c' e as figuras,  'Jc', 'Qc', 'Kc'.

#Dica: para juntar duas strings, faça nova='a'+'b'
#Dica: para transformar um numero n em string, faça str(n)

#escreva um código que cria um baralho completo, com todas as 52 cartasela nao recebe nada e produz uma lista.os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus) as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K' O J de ouros, por exemplo, é representado pela string 'Jo'.  Assim 'Jo' é um dos elementos que deve aparecer na lista


naipe = input("Digite a primeira letra do naipe: ").upper()

if naipe == "O" or naipe == "C" or naipe == "E" or naipe == "P":
    print(f"A{naipe}")
    for num in range(1, 11, 1):
        print(f"{num}{naipe}")
    print(f"J{naipe}")
    print(f"Q{naipe}")
    print(f"K{naipe}")
else:
    print("Naipe não existente")


naipes = ["O", "C", "E", "P"]
numeros = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for naipe in naipes:
    for numero in numeros:
        print(f"{naipe}{numero}")
'''

'''
#EXERCÍCIO 06
#Dados uma lista e duas posicoes, troque os dois elementos que estão nessas duas posições


frutas = ["bananas","meloes","mixiricas","uvas"]
pos1 = int(input("Digite a primeira posicao que gostaria de trocar: "))
pos2 = int(input("Digite a segunda posicao que gostaria de trocar: "))

fruta1 = frutas[pos1]
fruta2 = frutas[pos2]

frutas.pop(pos1)
frutas.insert(pos1, fruta2)

frutas.pop(pos2)
frutas.insert(pos2, fruta1)

print(frutas)
'''


'''
#EXERCÍCIO 07
#Dados uma lista ache seu primeiro e ultimo elementos


frutas = ["bananas","meloes","mixiricas","uvas"]
quantidade = len(frutas)
quantidade = quantidade - 1
print(frutas[0])
print(frutas[quantidade])
'''


'''
#EXERCÍCIO 01 DESAFIO
#Desafio: busque entender a função sorted do python, e tente refazer o primeiro exercicio, maior preço, usando ela

precos = [100,45,78,9,200,13,300,2]
print((sorted(precos, reverse= True))[0])
'''


'''
#EXERCÍCIO 8
#Um restaurante resolveu fazer uma promoção: o item mais barato da sua conta passa a ser de graça
#1. Dada uma lista de preços, substitua o elemento mais barato por 0
#2. Dada uma lista de preços, calcule a conta total

precos = []
desconto = 0
minimo = 1
while minimo > 0:
    precos.append(float(input("Digite os valores a atribuir a conta, se quiser parar, digite um numero negativo: ")))
    minimo = min(precos) 

precos = sorted(precos)
precos.pop(0)
precos.insert(0, 0)
print(f"O preco dos itens ficou: {precos}")
print(f"O valor total da conta é: {sum(precos)}")
'''


''''''
#EXERCÍCIO 9 e 10
#Temos uma lista de pessoas que tem autorização para editar os arquivos referentes às aulas de python
#Dada essa lista de pessoas e um nome, verifique se esse nome é de uma pessoa autorizada
#Temos uma segunda lista, com as senhas
#Dada essa lista de pessoas e, um nome e uma senha, crie uma função que verifique se as credenciais são válidas (ou seja, a pessoa é autorizada e a senha está correta)

def functionUsuario(nome, pessoas):
    nome = pessoas.count(nome)
    return nome

def functionSenha(senha, senhas):
    senha = senhas.count(senha)
    return senha

pessoas = ['lucas','marcia','iris','mirtes','josé','caio']
senhas  = ['123l', 'ma_1215', 'cornea' ,'mexirica', 'grafos' ,'algebra']

nome = input("Digite seu nome para ver se tem autorização: ").lower()
senha = input("Digite sua senha: ")

nome = functionUsuario(nome, pessoas)
senha = functionSenha(senha, senhas)

if nome == 1 and senha == 1:
    print("Autorizado")
else:
    print("Nao Autorizado")
''''''