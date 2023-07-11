'''
#ALGARITIMO 01
tipo_cliente = str(input("Digite se voce e um cliente Premium (P) ou Normal (N): ")).upper()

if tipo_cliente == "PREMIUM" or tipo_cliente == "P":
    peso_bagagem = float(input("Digite o peso da bagagem: "))
    if peso_bagagem < 50:
        print("Peso dentro do permitido")
    else:
        print("Peso acima do permitido")
elif tipo_cliente == "NORMAL" or tipo_cliente == "N":
    peso_bagagem = float(input("Digite o peso da bagagem: "))
    if peso_bagagem < 28:
        print("Peso detro do permitido")
    else:
        print("Peso acima do permitido")
else:
    print("Tipo de cliente inválido")
'''




'''
#ALGARITIMO 02
nome = input("Digite seu nome: ").capitalize()
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome} sua autorização foi aceita")
else:
    autorizacao = input("Voce possui autorizacao dos responsáveis? S- Sim ou N- Nao: ").upper()
    if autorizacao == "S":
        print(f"{nome} sua autorização foi aceita")
    elif autorizacao == "N":
        print(f"{nome} sua autorização nao foi aceita pois nao tem idade o suficiente")
    else:
        print("Sua opcao e invalida")
'''




'''
#ALGARITIMO 03
pontos = int(input("Digite quantos pontos voce tem: "))

if pontos >= 1000:
    print("Voce terá 3GB adicionados a sua franquia")
elif 1000 > pontos >= 500:
    print("Voce terá 1,5GB adicionados a sua franquia")
elif  500 > pontos > 200:
    print("Voce terá 500MB adicionados a sua franquia")
else:
    print("Voce nao tera nenhum ponto adicionado")
'''




'''
#ALGORITIMO TESTE 01
valor_compra = float(input("Digite o valor da sua compra: "))
forma_pagamento = int(input("Digite a sua forma de pagamento para 1- Dinheiro ou 2- Outros: "))

if valor_compra > 100 and forma_pagamento == 1:
    valor_compra = (valor_compra - (1/10 * valor_compra))
    print(f"{valor_compra} e o valor da sua compra final")
else:
    print(f"{valor_compra} e o valor da sua compra final")
'''




'''
#ALGORITIMO 05
valor_compra = float(input("Digite o valor da sua compra: "))
cupom_desconto = str(input("Digite o cupom de desconto: ")).upper()

if cupom_desconto == "NIVER10":
    valor_compra = valor_compra - (1/10 * valor_compra)
print(f"O valor final da sua compra e {valor_compra}")
'''




'''
#ALGORITIMO TESTE 02
import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b * b) - 4 * a * c

if delta > 0 :
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"O primeiro valor de X1 e {round(x1 , 3)} e o X2 e {round(x2 , 3)}")
elif delta == 0:
    x1 = (-b) / (2 * a)
    print(f"O unico valor de X e {round(x1 , 3)}")
else:
    print(f"Valor de X nao pode ser calculado pois o valor de delta({round(delta , 3)}) é negativo")
'''




'''
#ALGORITIMO TESTE 03
bpm = int(input("Digite os seus batimentos por minuto(BPM): "))
idade = int(input("Digite sua idade: "))

if idade < 3:
    if bpm < 120:
        print(f"Sua BPM esta BAIXO para {idade} anos")
    elif bpm <= 140:
         print(f"Sua BPM esta NORMAL para {idade} anos")
    else:
        print(f"Sua BPM esta ALTA para {idade} anos")
elif idade < 18:
    if bpm < 80:
        print(f"Sua BPM esta BAIXO para {idade} anos")
    elif bpm <= 100:
         print(f"Sua BPM esta NORMAL para {idade} anos")
    else:
        print(f"Sua BPM esta ALTA para {idade} anos")
elif idade < 61:
    if bpm < 70:
        print(f"Sua BPM esta BAIXO para {idade} anos")
    elif bpm <= 80:
         print(f"Sua BPM esta NORMAL para {idade} anos")
    else:
        print(f"Sua BPM esta ALTA para {idade} anos")
else:
    if bpm < 50:
        print(f"Sua BPM esta BAIXO para {idade} anos")
    elif bpm <= 60:
         print(f"Sua BPM esta NORMAL para {idade} anos")
    else:
        print(f"Sua BPM esta ALTA para {idade} anos")
'''




'''
#ALGORITIMO TESTE 04
valor_bruto = float(input("Digite o valor da viagem: "))
assentos = str(input("Digite o tipo de assento: ")).upper()
quantidade = int(input("Digite a quantidade de viajantes: "))

if assentos == "ECONOMICA":
    if quantidade <= 2:
        desconto = (3/100 * valor_bruto)
    elif quantidade == 3:
        desconto = (4/100 * valor_bruto)
    else:
        desconto = (5/100 * valor_bruto)
elif assentos == "EXECUTIVO":
    if quantidade <= 2:
        desconto = (5/100 * valor_bruto)
    elif quantidade == 3:
        desconto = (7/100 * valor_bruto)
    else:
        desconto = (8/100 * valor_bruto)
elif assentos == "PRIMEIRA CLASSE":
    if quantidade <= 2:
        desconto = (1/10 * valor_bruto)
    elif quantidade == 3:
        desconto = (15/100 * valor_bruto)
    else:
        desconto = (2/10 * valor_bruto)
else:
    print("Tipo de assento invalido")

valor_final = valor_bruto - desconto
valor_medio = valor_final / quantidade
print(f"Valor Bruto: R${valor_bruto}\nValor do Desconto: R${desconto}\nValor Liquido da Viagem: R${valor_final}\nValor Medio: R${valor_medio}")
'''




'''
#ALGORITIMO TESTE 05
escolha01 = str(input("Digite a escolha do primeiro: ")).upper()
escolha02 = str(input("Digite a escolha do segundo: ")).upper()
escolha03 = str(input("Digite a escolha do terceiro: ")).upper()
escolha04 = str(input("Digite a escolha do quarto: ")).upper()
escolha05 = str(input("Digite a escolha do quinto: ")).upper()

p = 0
x = 0
n = 0
i = 0

if escolha01 == "PLAYSTATION":
    p = p + 1
elif escolha01 == "XBOX":
    x = x + 1
elif escolha01 == "NINTENDO":
    n = n + 1
else:
    i = i + 1

if escolha02 == "PLAYSTATION":
    p = p + 1
elif escolha02 == "XBOX":
    x = x + 1
elif escolha02 == "NINTENDO":
    n = n + 1
else:
    i = i + 1

if escolha03 == "PLAYSTATION":
    p = p + 1
elif escolha03 == "XBOX":
    x = x + 1
elif escolha03 == "NINTENDO":
    n = n + 1
else:
    i = i + 1

if escolha04 == "PLAYSTATION":
    p = p + 1
elif escolha04 == "XBOX":
    x = x + 1
elif escolha04 == "NINTENDO":
    n = n + 1
else:
    i = i + 1

if escolha05 == "PLAYSTATION":
    p = p + 1
elif escolha05 == "XBOX":
    x = x + 1
elif escolha05 == "NINTENDO":
    n = n + 1
else:
    i = i + 1

if p > x and x >= n:
    print("PlayStation ganhou")
elif x > p and p >= n:
    print("Xbox ganhou")
elif n > p and p >= x:
    print("Nintendo ganhou")
else:
    print("Houve empate")

print(f"Escolheram PlayStation: {p} \nEscolheram Xbox: {x} \nEscolheram Nintendo: {n} \nEscolheram Opcao Invalida: {i}")
'''




'''
#ALGORITIMO TESTE 05 EVOLUÇÃO

cont = 0
p = 0
x = 0
n = 0

while cont < 5:
    escolha = int(input("Digite sua escolha com 1- PlayStation, 2- Xbox, 3- Nintendo: "))
    if escolha == 1:
        p = p + 1
    elif escolha == 2:
        x = x + 1
    elif escolha == 3:
        n = n + 1
    else:
        print("Opcao invalida")
    cont = cont + 1

if p > x and x >= n:
    print("PlayStation ganhou")
elif x > p and p >= n:
    print("Xbox ganhou")
elif n > p and p >= x:
    print("Nintendo ganhou")
else:
    print("Houve empate")
print(f"Escolheram PlayStation: {p} \nEscolheram Xbox: {x} \nEscolheram Nintendo: {n}")
'''