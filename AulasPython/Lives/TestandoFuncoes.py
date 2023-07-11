
# TESTANDO IF E ELSE
#nome = input("Digite seu nome:").upper()

#if nome == "AAA":
#    print("Você digitou AAA")
#else:
#    print("Você digitou não AAA")


# TESTANDO PRINCIPAIS TAGS
#primeiro_valor = int(input("Escreva o primeiro número:"))
#segundo_valor = int(input("Escreva o primeiro número:"))
#soma = primeiro_valor + segundo_valor
#print(f"A soma é: {soma}")


#COLOCANDO EM PRÁTICA AS PRINCIPAIS TAGS
ano_nascimento = int(input("Digite o ano em que voce nasceu: ")) 
aniversario = input("Voce ja fez aniversario esse ano? (Responda com Sim ou Nao): ").upper() 
ano_2023 = input("Voce continua em 2023? (Responda com Sim ou Nao): ").upper() 
 

if ano_2023 == "SIM": 
    if aniversario == "SIM": 
        idade = 2023 - ano_nascimento 
        print (f"Sua idade é: {idade}") 
    else: 
        idade = ((2023 - ano_nascimento) - 1)
        print (f"Sua idade é: {idade}") 
else: 
    ano_atual = int(input("Digite o ano em que voce esta: ")) 
    if ano_nascimento <= ano_atual: 
        if aniversario == "SIM": 
            idade = ano_atual - ano_nascimento 
            print (f"Sua idade é: {idade}") 
        else: 
            idade = ((ano_atual - ano_nascimento) - 1)
            print (f"Sua idade é: {idade}") 
    else: 
        print("VAI SE FUDE SEU BURRO, NAO SABE DIGITAR") 
