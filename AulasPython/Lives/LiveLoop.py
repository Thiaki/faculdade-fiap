#https://drive.google.com/drive/folders/1ShDroMo3SrzB-YjbXwjJcFqIdD4o9pWE
'''
#EXERCÍCIO 01
# Sua missão: pedir ao usuário um ddd e um telefone, e verificar se os dados fornecidos
# são válidos. 

# Consideraremos que um telefone válido tem 9 digitos e começa necessariamente por 9
# Assim, 
#* 988887733 é um telefone válido, 
#* 999888 não é, 
#* 899009988 não é
#* 9999999999 não é (10 numeros 9 seguidos, grande demais)
# (essa regra está obviamente errada, mas faz um exercicio interessante)

# Consideramos um ddd válido se ele tiver 2 digitos. Ou seja, se ele for maior ou igual a 10, e menor que 100

# Suas ferramentas:
# * input, para pedir texto ao usuário
# * converter string para numero:
# a = input("digite o ddd: ")      #resulta uma string, um texto, como "11"
# a = int(input("digite o ddd: ")) #um número, como 11
# * operadores de comparação
# if (a > 10):
#   print("o numero {} é maior que 10".format(a))

ddd = int(input("Digite o seu ddd: "))
numero = int(input("Digite o seu número de telefone: "))
if 10 < ddd < 100 and 899999999 < numero < 1000000000:
    print("Seu número é correto")
else:
    print("Seu número não é correto")
'''


'''
#EXERCÍCIO 02
# https://www.cnnbrasil.com.br/perguntas-frequentes/eleicoes/titulo-de-eleitor/quem-pode-votar-no-brasil/

# Sua missão: receber dados de uma pessoa, e dizer se o voto é
# OBRIGATORIO, FACULTATIVO ou NAO PERMITIDO

# Os dados da pessoa: idade, número inteiro em anos
# Alfabetizado(a): string, com os possiveis valores "SIM" ou "NAO"

# Suas ferramentas:
# * if, elif, else, and e or
# * converter string para numero:
# a = input("digite o ano") resulta uma string, um texto, como "1984"
# a = int(input("digite o ano")) um número, como 1984
# * comparar valores

#a = 20
#alfa = "NAO"

#if a > 10:
#    print("ola")  # esse ola so é exibido se a for maior que 10. Se você mudar na linha de cima, ele não será exibido
#if alfa == "SIM":
#    print("alfabetizado")  # esse alfabetizado so é exibido se a variável alfa tiver a string "SIM"

# Desafio 1: aceite "Sim", "sim" como valores para alfabetizado
# Desafio 2: Reclame se o usuário digitar algo diferente de "sim" e "nao",
# mas aceitando as variações de maiúscula e minúscula

nome = input("Digite seu nome: ").capitalize()
ano_nascimento = int(input(f"{nome}, digite o seu ano de nascimento: "))
alfabetizacao = input(f"{nome}, voce e alfabetizado? ").upper()
idade = 2023 - ano_nascimento

if alfabetizacao == "SIM" or alfabetizacao == "NAO":
    if idade == 16 or idade == 17 or idade > 70 or alfabetizacao == "NAO":
        print("Votacao facultativa")
    elif 18 <= idade <= 70:
        print("Votacao obrigatória")
    elif idade < 16:
        print("Votacao nao permitida")
else:
    print("Opcao invalida, tente novamente")
'''


'''
#EXERCÍCIO 03
# Sua missão: receber três alturas de pessoas, e imprimir a média
# As alturas são números reais (como 2.12, ou 1.78)

# Suas ferramentas:
# * pedir um número real para o usuário
# a = input("digite um numero: ")          #a é um texto, como "1.78"
# a = float(input("digite um numero: "))   #a é um numero,como  1.78
# * somar numeros
# soma = a + 10 + 30
# * dividir
# media = soma/2


# Desafio: se algum dos números for absurdo (por exemplo, maior do que 3 metros), seu programa deve alertar
# o usuário da existência de um possivel dado inválido

cont = 0
soma_altura = 0
pessoas_sem_calculo = 0
pessoas = int(input("Digite a altura de quantas pessoas vai somar a média: "))
while pessoas != cont:
    altura = float(input("Digite a altura da pessoa: "))
    if altura > 2.50:
        print("A altura que voce digitou provavelmente esta errada, ela nao entrara no calculo.")
        pessoas_sem_calculo = pessoas_sem_calculo + 1
    else:
        soma_altura = soma_altura + altura
        media_altura = soma_altura / (pessoas - pessoas_sem_calculo)
    cont = cont + 1
print(f"Media das alturas e: {media_altura}")
'''

'''
#EXERCÍCIO 04
# https://cmpprev.com.br/blog/idade-minima-para-aposentadoria-entenda-as-novas-regras/

# Sua missão: receber uma idade, um total de anos de contribuição, e o sexo, e responder se
# a pessoa já pode pedir a aposentadoria. (escrevendo "PODE" ou "NAO PODE")
# Consideraremos a regra para trabalhadores urbanos, descrita no link

# Detalhes: o sexo será enviado como "homem" ou "mulher"

# Suas ferramentas:
# * pedir um texto para o usuário
# a = input("digite o texto")
# * pedir um número inteiro para o usuário
# b = int(input("digite o número"))
# * operador logico or
#if (a == "mulher" or b > 10): #se a == "mulher", OU b > 10, não precisa ser os 2, o print ocorre
#    print ("pode 1")
# * operador logico and
#if (a == "mulher" and b > 10): #se a == "mulher", E b > 10, precisa ser os 2 ao mesmo tempo, o print ocorre
#    print ("pode 2")

# Desafio: Se o usuario escrever "Mulher", "MULHER" ou qualquer outro uso de maiúsculas, seu programa deve funcionar.
# Se escrever qualquer coisa que não seja "homem" nem "mulher", seu programa deve reclamar, e não imprimir
# nem "PODE" nem "NAO PODE"

idade = int(input("Digite sua idade: "))
anos_contribuicao = int(input("Digite os anos de contribuicao: "))
sexo = input("Digite seu sexo: ").upper()

if sexo != "HOMEM" and sexo != "MULHER":
    print("Sexo invalido, favor revisar")
else:
    if sexo == "HOMEM" and idade > 65 and anos_contribuicao > 20:
        print("PODE")
    elif sexo == "MULHER" and idade > 62 and anos_contribuicao > 15:
        print("PODE")
    else:
        print("NAO PODE")
'''


'''
#EXERCÍCIO 05
# https://pt.wikipedia.org/wiki/Ano_bissexto#Calend%C3%A1rio_Gregoriano

# Sua missão: escrever um programa que recebe o número de um ano, e determina se
# ele é ou não bissexto

# suas ferramentas:
# * if, elif, else
# * operador modulo: para saber se um número é multiplo de 4, podemos fazer
# n%4. Isso devolve o resto da divisão por 4. Se esse resto for zero, o número
# é multiplo de 4
# * converter string para numero:
# a = input("digite o ano") resulta uma string, um texto, como "1984"
# a = int(input("digite o ano")) um número, como 1984

#a = int(input("digite o ano"))
#print(a % 4)
#if a % 4 == 0:
#    print("o numero {} é multiplo de 4".format(a))

ano = int(input("Digite um ano para saber se ele e bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Ano Bissexto")
else:
    print("Ano nao bissexto")
'''


'''
#EXERCÍCIO 06
# Sua missão: receber uma hora e um minuto, e dizer o valor do tempo atual e
# do tempo um minuto depois

# Se o usuário digitar uma hora maior ou igual a 24, ou um minuto maior ou igual a 60, reclame
# e NAO faça mais nada

# Exemplos: se o usuário digitar 10 para horas, 12 para minutos
# Imprimir:       Tempo atual: 10:12
#                Tempo futuro: 10:13

# Exemplos: se o usuário digitar 1 para horas, 59 para minutos
# Imprimir:       Tempo atual: 01:59
#                Tempo futuro: 02:00

# Exemplos: se o usuário digitar 23 para horas, 59 para minutos
# Imprimir:       Tempo atual: 23:59
#                Tempo futuro: 00:00

# Exemplos: se o usuário digitar 35 para horas, 59 para minutos
# Imprimir:      Valor invalido para horas

#Suas ferramentas:
# * operadores condicionais if/elif/else
# * para imprimir um número, podemos fazer assim
# h=12
# m=3
# print("O horário atual é {:02d}:{:02d}".format(h,m))
#note que já coloquei um código específico para garantir que um zero será adicionado na frente, mas apenas quando necessário

horas = int(input("Digite o valor das horas: "))
minutos = int(input("Digite o valor dos minutos: "))

if horas > 24 or minutos > 60:
    print("Valor inválido")
else:
    minutos_futuro = minutos + 1
    if minutos_futuro == 60:
        minutos_futuro = 00
        horas_futuro = horas + 1
    if horas_futuro == 25:
        horas_futuro = 1 
        
    print(f"Tempo atual: {horas:02d}:{minutos:02d}")
    print(f"Tempo futuro: {horas_futuro:02d}:{minutos_futuro:02d}")
'''



'''
#EXERCÍCIO 07
#https://economia.uol.com.br/imposto-de-renda/noticias/redacao/2023/02/28/tabela-do-imposto-de-renda-2023-veja-faixas-aliquotas-e-como-calcular.htm

#Sua missão: dado um salário mensal fixo, calcular o valor do imposto de renda (mensal) correspondente
# Não esqueça de consultar no link, temos que tomar uma porcentagem E aplicar um desconto, dependendo
# da faixa de renda do individuo

#Suas ferramentas:
# * Ler um número real
# * Condicionais if/else/elif

salario = float(input("Digite seu salario: "))

if salario <= 1903.98:
    print("Voce nao precisa pagar nada")
elif 1903.99 <= salario <= 2826.65:
    pagar = (salario * 7.5/100) - 142.80
    print(f"Voce deve pagar {pagar:.2f}")
elif 2826.66 <= salario <= 3751.05:
    pagar = (salario * 15/100) - 354.80
    print(f"Voce deve pagar {pagar:.2f}")
elif 3751.06 <= salario <= 4664.68:
    pagar = (salario * 22.5/100) - 636.13
    print(f"Voce deve pagar {pagar:.2f}")
elif salario > 4664.68:
    pagar = (salario * 27.5/100) - 869.36
    print(f"Voce deve pagar {pagar:.2f}")
'''



'''
#EXERCÍCIO 08
# Na empresa, três setores estão competindo para ver quem consegue um aumento maior nas vendas.

# Sua missão: construa um algoritmo que, para da uma das equipes, receba:
# 1. O nome do setor
# 2. O valor de vendas no mês anterior (um número inteiro)
# 3. O valor de vendas no mês atual (um número inteiro)

# Ele deve imprimir:
# 1. O crescimento das vendas para cada setor
# 2. O nome do setor vencedor

# Suas ferramentas
# * Condicional if


# Desafio: imprimir também, para cada setor, o aumento percentual das vendas, com duas casas decimais
# * Para imprimir números com duas casas decimais, podemos fazer o seguinte
# x = 3.14159
# print('O valor de x é {:.2f}'.format(x))  # imprime "O valor de x é 3.14"

nome1 = input("Digite o nome do seu setor: ")
mes_anterior1 = int(input("Digite o valor de vendar no mes anterior: "))
mes_atual1 = int(input("Digite o valor de vendar no mes atual: "))

nome2 = input("\nDigite o nome do seu setor: ")
mes_anterior2 = int(input("Digite o valor de vendar no mes anterior: "))
mes_atual2 = int(input("Digite o valor de vendar no mes atual: "))

nome3 = input("\nDigite o nome do seu setor: ")
mes_anterior3 = int(input("Digite o valor de vendar no mes anterior: "))
mes_atual3 = int(input("Digite o valor de vendar no mes atual: "))
print("\n")

crescimento1 = mes_atual1 - mes_anterior1
crescimento2 = mes_atual2 - mes_anterior2
crescimento3 = mes_atual3 - mes_anterior3

if crescimento1 > crescimento2 and crescimento1 > crescimento3:
    print(f"Equipe {nome1} faturou mais")
elif crescimento2 > crescimento1 and crescimento2 > crescimento3:
    print(f"Equipe {nome2} faturou mais")
elif crescimento3 > crescimento1 and crescimento3 > crescimento2:
    print(f"Equipe {nome3} faturou mais")
else:
    print("Teve empate nas vendas")
print("\n")

if crescimento1 >= 0:
    crescimento1_percentual = ((mes_atual1 - mes_anterior1) / mes_anterior1) * 100
    print(f"Cresimento das vendas da equipe {nome1} foi {crescimento1}")
    print(f"Cresimento percentual foi de {crescimento1_percentual:.2f}%")
else:
    crescimento1 = - 1 * crescimento1
    crescimento1_percentual = ((mes_anterior1 - mes_atual1) / mes_atual1) * 100
    print(f"A equipe {nome1} abaixou as vendas em {crescimento1}")
    print(f"Teve queda de percentual {crescimento1_percentual:.2f}%")

if crescimento2 >= 0:
    crescimento2_percentual = ((mes_atual2 - mes_anterior2) / mes_anterior2) * 100
    print(f"Cresimento das vendas da equipe {nome2} foi {crescimento2}")
    print(f"Cresimento percentual foi de {crescimento2_percentual:.2f}%")
else:
    crescimento2 = - 1 * crescimento2
    crescimento2_percentual = ((mes_anterior2 - mes_atual2) / mes_atual2) * 100
    print(f"A equipe {nome2} abaixou as vendas em {crescimento2}")
    print(f"Teve queda de percentual {crescimento2_percentual:.2f}%")

if crescimento3 >= 0:
    crescimento3_percentual = ((mes_atual3 - mes_anterior3) / mes_anterior3) * 100
    print(f"Cresimento das vendas da equipe {nome3} foi {crescimento3}")
    print(f"Cresimento percentual foi de {crescimento3_percentual:.2f}%")
else:
    crescimento3 = - 1 * crescimento3
    crescimento3_percentual = ((mes_anterior3 - mes_atual3) / mes_atual3) * 100
    print(f"A equipe {nome3} abaixou as vendas em {crescimento3}")
    print(f"Teve queda de percentual {crescimento2_percentual:.2f}%")
'''


'''
#EXERCÍCIO 08 UPGRADE
for x in range(1,4):
    nome = input("Digite o nome do seu setor: ")
    mes_anterior = int(input("Digite o valor de vendar no mes anterior: "))
    mes_atual = int(input("Digite o valor de vendar no mes atual: "))

    crescimento = mes_atual - mes_anterior
    if x == 1:
        crescimento1 = crescimento
        nome1 = nome
    elif x == 2:
        crescimento2 = crescimento
        nome2 = nome
    elif x== 3:
        crescimento3 = crescimento
        nome3 = nome

    if crescimento >= 0:
        crescimento_percentual = ((mes_atual - mes_anterior) / mes_anterior) * 100
        print(f"Cresimento das vendas da equipe {nome} foi {crescimento}")
        print(f"Cresimento percentual foi de {crescimento_percentual:.2f}%")
    else:
        crescimento = - 1 * crescimento
        crescimento_percentual = ((mes_anterior - mes_atual) / mes_atual) * 100
        print(f"A equipe {nome} abaixou as vendas em {crescimento}")
        print(f"Teve queda de percentual {crescimento_percentual:.2f}%")
    

if crescimento1 > crescimento2 and crescimento1 > crescimento3:
    print(f"Equipe {nome1} faturou mais")
elif crescimento2 > crescimento1 and crescimento2 > crescimento3:
    print(f"Equipe {nome2} faturou mais")
elif crescimento3 > crescimento1 and crescimento3 > crescimento2:
    print(f"Equipe {nome3} faturou mais")
else:
    print("Teve empate nas vendas")
'''