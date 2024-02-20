package br.com.fiap.aula01;
import java.util.Scanner;

public class ArrayExercicios {

	public static void main(String[] args) {
		
		/* Exercício 1:
		 * Escreva um programa para preencher uma matriz unidimensional (vetor) com 15 posições de números inteiros e, em seguida, apresente os elementos. - Pesquisa Google.
		 */
		
		/* Exercício 2:
		 * Escreva um programa para preencher uma matriz unidimensional (vetor) que deverá receber as temperaturas ao longo do dia. A medição precisa ser registrada a cada uma hora. Ao final, exiba a temperatura média do dia.
		 */
		
		/* Exercício 3:
		 * Altere o programa anterior para registrar as temperaturas de cada dia do mês, neste caso, utilize uma matriz com 30 linhas e 24 colunas. Ao final, verifique qual foi a maior temperatura, a menor temperatura e a temperatura média.
		 */
		
		/* Exercício 4:
		 * Escreva um programa para armazenar em uma matriz as notas das 5 disciplinas dos 20 alunos de uma turma.
		 */
		
		
		// ---------------------------------- //
		
		
		Scanner sc = new Scanner(System.in);
		
		// Exercício 1
		
		int numero[] = new int[15];
		for (int i = 0 ; i < numero.length ; i++) {
			System.out.print("Digite o " + (i + 1) + "° valor: ");
			numero[i]= sc.nextInt();
		}
		System.out.println("----------------");		
		for (int contador = 0 ; contador < numero.length ; contador++) {
			System.out.println((contador + 1) + "° numero - " + numero[contador]);
		}
		
		
		// ---------------------------------- //
		
		// Exercicio 2
		
		double temperatura[] = new double[24];
		double somaTemperatura = 0;
		for (int i = 0 ; i < temperatura.length ; i++) {
			System.out.print("Digite a temperatura das " + (i + 1) + "hrs: ");
			temperatura[i] = sc.nextDouble();
			somaTemperatura += temperatura[i];
		}
		System.out.print("A média de temperatura nesse dia foi de: " + (somaTemperatura/(temperatura.length)));
		
		
		// ---------------------------------- //
		
		// Exercicio 3
		
		double temperatura1[][] = new double[30][24];
		double somaTemperatura1 = 0;
		double maiorTemperatura = Double.NaN;
		double menorTemperatura = Double.NaN;
		int contTemperatura = 0;
		
		for (int i = 0 ; i < 30 ; i++) {
			for (int cont = 0 ; cont < 24 ; cont++) {
				System.out.print("Digite a temperatura das " + (cont + 1) + "hrs do dia " + (i + 1) + ": ");
				temperatura1[i][cont] = sc.nextDouble();
				somaTemperatura1 += temperatura1[i][cont];
				contTemperatura ++;
				
				if (Double.isNaN(maiorTemperatura)) {					
					maiorTemperatura = temperatura1[i][cont];
				}
				else {					
					if (temperatura1[i][cont] > maiorTemperatura) {
						maiorTemperatura = temperatura1[i][cont];
					}
				}
				
				if (Double.isNaN(menorTemperatura)) {					
					menorTemperatura = temperatura1[i][cont];
				}
				else {					
					if (temperatura1[i][cont] < menorTemperatura) {
						menorTemperatura = temperatura1[i][cont];
					}
				}
			}
			System.out.println("--------");
		}
		double mediaTemperatura = somaTemperatura1/contTemperatura;
		System.out.println("A média das temperaturas é: " + mediaTemperatura);
		System.out.println("A maior temperatura é: " + maiorTemperatura);
		System.out.println("A menor temperatura é: " + menorTemperatura);
		
		
		// ---------------------------------- //
		
		// Exercicio 4
		
		// Array Alunos [nome][nota]
		int numAlunos = 3;
		int numDisciplinas = 2;

		double[][] notas = new double[numAlunos][numDisciplinas];

		for (int aluno = 0; aluno < numAlunos; aluno++) {
			System.out.println("Notas do aluno " + (aluno + 1) + ":");
			for (int disciplina = 0; disciplina < numDisciplinas; disciplina++) {
				System.out.print("Digite a nota da disciplina " + (disciplina + 1) + ": ");
				notas[aluno][disciplina] = sc.nextDouble();
			}
		}

		System.out.println("\nNotas dos alunos:");
		for (int aluno = 0; aluno < numAlunos; aluno++) {
			System.out.print("Aluno " + (aluno + 1) + ": ");
			for (int disciplina = 0; disciplina < numDisciplinas; disciplina++) {
				System.out.print(notas[aluno][disciplina] + " ");
			}
			System.out.println();
		}	
		sc.close();
		
	}
	
}
