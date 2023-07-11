#1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

#Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
#Nível  -  Porcentagem sobre o faturamento
#Basic  -  30%
#Silver  -  20%
#Gold  -  10%
#Platinum  -  5%

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