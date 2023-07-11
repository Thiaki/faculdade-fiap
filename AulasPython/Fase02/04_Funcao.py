def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

operacao = input("Qual sera a operacao? ")

if operacao == "+":
    print(soma(a, b))
elif operacao == "-":
    print(subtracao(a, b))
elif operacao == "*":
    print(multiplicacao(a, b))
elif operacao == "/":
    print(divisao(a, b))
else:
    print("Operacao invalida")