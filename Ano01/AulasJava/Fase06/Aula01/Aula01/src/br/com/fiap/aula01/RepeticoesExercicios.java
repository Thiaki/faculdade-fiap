package br.com.fiap.aula01;
import java.util.Scanner;

public class RepeticoesExercicios {

	public static void main(String[] args) {
		
		/* Exercício 1:
		 * Elabore um programa para ler 20 valores inteiros fornecidos pelo usuário e calcular a soma deles. Apresente o resultado ao final.
		 */
		
		/* Exercício 2:
		 * Elabore um programa para fazer a tabuada de um número fornecido pelo usuário, variando de 0 até 12, e mostre o resultado de cada iteração.
		 */
		
		/* Exercício 3:
		 * Elabore um programa que calcule a sequência de Fibonacci até 30° termo. A sequência obedece ao seguinte padrão: 1, 1, 2, 3, 5, n. (Somando o número anterior ao antes dele)
		 */
		
		/* Exercício 4:
		 * Elabore um programa que leia o nome e o salário de n pessoas, o usuário deverá informar se deseja continuar a interação. Ao final, apresente a quantidade de pessoas informadaas e a média entre os salários.
		 */
		
		
		// ---------------------------------- //
		
		
		Scanner sc = new Scanner(System.in);
		
		//Exercício 01
		
		int result = 0;
		for (int cont = 1 ; cont < 21 ; cont++) {
			System.out.print("Digite o " + cont + "° número: ");
			int soma = sc.nextInt();
			result = result + soma;
		}
		System.out.print("O resultado das somas é: " + result);
		
		
		// ---------------------------------- //
		
		// Exercício 2
		
		int escolha;	
		do {
		System.out.print("Digite um número de 0 a 12 e descubra a tabuada dele: ");
		escolha = sc.nextInt();
		} while (escolha < 0 || escolha > 12);
		
		System.out.print("Você quer que sua tabuada vá até que número? ");
		int tabuadaFinal = sc.nextInt();
		tabuadaFinal++;
		
		for (int tabuada = 0 ; tabuada < tabuadaFinal ; tabuada++) {
			System.out.println(escolha + " * " + tabuada + " = " + (escolha * tabuada));
		}
		
		
		// ---------------------------------- //
		
		// Exercício 3
		
		int contador1 = 0;
		int contador2 = 1;
		int conts = 0;
		
		System.out.println("Digite até que número você quer a sequência de Fibonacci: ");
		int fibonacci = sc.nextInt();
		fibonacci--;
		
		System.out.print(contador2 + " ");
		
		while (conts < fibonacci) {
			int temporario = contador1 + contador2;
			System.out.print(temporario + " ");
			contador1 = contador2;
			contador2 = temporario;
			conts++;
		}		
		
		
		// ---------------------------------- //
		
		// Exercício 4

		String continuar;
		int quantidade = 0;
		double salario;
		double totalSalario = 0;
		double mediaSalario;
		
		do {
			System.out.print("Digite o nome da pessoa: ");
			String nome = sc.nextLine();
			
			System.out.print("Digite o salário da pessoa: ");
			salario = sc.nextDouble();
			sc.nextLine();
			
			totalSalario = totalSalario + salario;
			quantidade++;
			
			System.out.print("Deseja continuar o programa?(S/N) ");
			continuar = sc.nextLine();
			System.out.println(continuar);
		} while(continuar.equalsIgnoreCase("S"));
		
		mediaSalario = (totalSalario / quantidade);
		
		System.out.println("A quantidade de pessoas foi: " + quantidade);
		System.out.println("A média dos salários foi: " + mediaSalario);
		
		
		
		sc.close();
	}
}
