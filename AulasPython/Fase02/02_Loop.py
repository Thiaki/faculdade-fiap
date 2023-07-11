'''
#TESTE 02
x = 0
total_gasto = 0
transacoes = int(input("Digite quantas transacoes voce fez: "))
while x != transacoes:
    valor = float(input("Digite o valor da transacao: "))
    total_gasto = total_gasto + valor
    media_gasto = total_gasto / transacoes
    x = x + 1
print(f"O total gasto e {total_gasto:.2f}")
print(f"A media das transacoes e {media_gasto:.2f}")
print("Obrigado por usar!")
'''



'''
#TESTE 03
num1 = 1
num2 = 0
num3 = 1
numero = int(input("Digite um numero inteiro: "))

for x in range(0, numero + 1):
    num1 = num2 + 0
    num2 = num3 + 0
    num3 = num1 + num2
    if numero == num3:
        print("Fibonacci ok")
        break
    elif numero < num3:
        print("fibonaci nao")
        break
'''