import CalculadoraModulo #Assim indica o arquivo "CalculadoraModulo.py", mas vai precisar colocar o nome do arquivo antes das funções usadas, exemplo: CalculadoraModulo.soma ou CalculadoraModulo.subtracao
from CalculadoraModulo import soma, subtracao #Assim trás as funções "soma" e "subtracao" do arquivo "CalculadoraModulo.py"
from CalculadoraModulo import * #Assim trás TODAS as funções do arquivo "CalculadoraModulo.py"

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

print(soma(a, b))
print(subtracao(a, b))
print(divisao(a, b))
print(multiplicacao(a, b))