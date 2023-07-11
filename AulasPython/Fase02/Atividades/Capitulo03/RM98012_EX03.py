#3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:

#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

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