package br.com.fiap.exercicio;
import java.util.Scanner;
import java.text.DecimalFormat;

public class deposito {
	public static void main(String[] args) { 
		Scanner sc = new Scanner(System.in);
		DecimalFormat df = new DecimalFormat(".00");

		System.out.print("Digite o quanto foi depositado: ");
		double deposito = sc.nextDouble();

		System.out.print("Foi depositado: " + (df.format(deposito)));
		sc.close();
	}
}