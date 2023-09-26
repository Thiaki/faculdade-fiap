package br.com.fiap.aula01;
import java.util.Scanner;

public class Array {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// Criando um array nota
		// int nota[];
		
		// Especificando o tamanho do array
		// int notas[] = new int[3];
		
		// Colocando o valor 10 no indice 0
		// notas[0] = 10;
		// System.out.println(notas[0]);
		
		// Colocando vários valores em uma ARRAY NOVA
		// int nota[] = {10, 9, 8, 2};
		
		float[] notas = new float[10];
		for (int cont=0; cont<10; cont++) {
		  System.out.println("Digite a nota do aluno");
		  notas[cont] = sc.nextFloat();
		}
		
		
		sc.close();
	}
	
}
