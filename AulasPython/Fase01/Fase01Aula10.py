'''
def escrever_result():
    print(f"Seu resultado é: {round(resultado, 2)}")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operacao que deseja (+ , - , / , *): ")

if operacao == "+":
    resultado =  valor1 + valor2
    escrever_result()
elif operacao == "-":
    resultado = valor1 - valor2
    escrever_result()
elif operacao == "/":
    resultado = valor1 / valor2
    escrever_result()
elif operacao == "*":
    resultado = valor1 * valor2
    escrever_result()
else:
    print("Comando que você digitou é inválido.\nTente novamente.")
'''
numero1 = int(input("Digite o primeiro numero da tabuada: "))
numero2 = int(input("Digite o segundo numero da tabuada: "))
tabuada = range(numero1 , (numero2 + 1))

for primeiro_numero in tabuada:
    print(f"\nTabuada do {primeiro_numero}")
    for segundo_numero in  tabuada:
        resultado = primeiro_numero * segundo_numero
        print(f"{primeiro_numero} X {segundo_numero} = {resultado}")
