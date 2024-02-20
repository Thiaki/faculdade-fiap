#2- Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

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