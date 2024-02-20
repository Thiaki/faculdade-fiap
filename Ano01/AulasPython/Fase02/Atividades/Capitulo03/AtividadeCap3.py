#1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
#Nível  -  Porcentagem sobre o faturamento
#Basic  -  30%
#Silver  -  20%
#Gold  -  10%
#Platinum  -  5%
'''
#RESPOSTA EXERCÍCIO 01:
tipo_assinatura = input("Digite qual sua assinatura: ").upper()
faturamento_anual = float(input("Digite seu faturamento anual: "))

if tipo_assinatura == "BASIC" and faturamento_anual >= 0:
    pagar = faturamento_anual * (3/10)
    print(f"Voce deve pagar R${pagar:.2f}")
elif tipo_assinatura == "SILVER" and faturamento_anual >= 0:
    pagar = faturamento_anual * (2/10)
    print(f"Voce deve pagar R${pagar:.2f}")
elif tipo_assinatura == "GOLD" and faturamento_anual >= 0:
    pagar = faturamento_anual * (1/10)
    print(f"Voce deve pagar R${pagar:.2f}")
elif tipo_assinatura == "PLATINUM" and faturamento_anual >= 0:
    pagar = faturamento_anual * (5/100)
    print(f"Voce deve pagar R${pagar:.2f}")
else:
    print("Voce digitou uma assinatura ou faturamento invalido, por favor tente novamente.")
'''

#---------------------------------------#

#2- Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.
'''
#RESPOSTA EXERCÍCIO 02:
segunda_feira = int(input("Digite quantas pessoas votaram na segunda-feira: "))
terca_feira = int(input("Digite quantas pessoas votaram na terca-feira: "))
quarta_feira = int(input("Digite quantas pessoas votaram na quarta-feira: "))
quinta_feira = int(input("Digite quantas pessoas votaram na quinta-feira: "))
sexta_feira = int(input("Digite quantas pessoas votaram na sexta-feira: "))
vencedor = 0

if segunda_feira > vencedor:
    vencedor = segunda_feira
    dia_vencedor = "segunda-feira"
if terca_feira > vencedor:
    vencedor = terca_feira
    dia_vencedor = "terca-feira"
if quarta_feira > vencedor:
    vencedor = quarta_feira
    dia_vencedor = "quarta-feira"
if quinta_feira > vencedor:
    vencedor = quinta_feira
    dia_vencedor = "quinta-feira"
if sexta_feira > vencedor:
    vencedor = sexta_feira
    dia_vencedor = "sexta-feira"
    
print(dia_vencedor)
'''

#---------------------------------------#

#3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:

#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
'''
#RESPOSTA EXERCÍCIO 03:
total_notas_impar = 0
total_notas_par = 0
for impar in range(1, 50, 2):    
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    nota_impar = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {impar}: "))
    total_notas_impar = total_notas_impar + nota_impar
    media_impar = total_notas_impar / 25

for par in range(2, 51, 2):    
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_par = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {par}: "))
    total_notas_par = total_notas_par + nota_par
    media_par = total_notas_par / 25

if media_impar > media_par:
    diferenca = media_impar - media_par
    print(f"A media impar venceu por uma diferenca de {diferenca} pontos")
elif media_par > media_impar:
    diferenca = media_par - media_impar
    print(f"A media par venceu por uma diferenca de {diferenca} pontos")
else:
    print("As duas metades empataram")
'''

#---------------------------------------#

#4 – Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. E é claro que os criminosos exigem um pagamento para informar a senha.

#Ao analisar o código do programa deles, porém, você descobre que a senha é composta pela palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.
'''
#RESPOSTA EXERCÍCIO 04:
fatorial = 1
minutos = int(input("Digite os minutos da sua maquina: "))
if 0 <= minutos <= 9:
    for cont in range(1, minutos + 1):
        fatorial = fatorial * cont
    print(f"Sua senha e: Liberdade{fatorial}")
else:
    print("Digite apenas o ultimo digito do horario")
'''