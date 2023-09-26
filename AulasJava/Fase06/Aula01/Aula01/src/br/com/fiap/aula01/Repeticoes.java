package br.com.fiap.aula01;

public class Repeticoes {
	
	public static void main(String[] args) {
		
		//WHILE	
		/*
		while(<condição>){
			<instrução>;
		}
		 */
	
		int numeroWhile = 0;
	
		while (numeroWhile < 10) {
			numeroWhile ++;
			System.out.println(numeroWhile);
		}
		
		System.out.println("<------------------->");
		
		//DO WHILE
		
		/*
		 do {
			<instrução>;
		} while (<condição>);
		 */
		
		int numeroDoWhile = 0;
		do {
			numeroDoWhile ++;
			System.out.println(numeroDoWhile);
		} while(numeroDoWhile < 10);
		
		System.out.println("<------------------->");
		
		//FOR
		
		/*
		 for (<condição>) {
		 	<instrução>
		 }
		 */
		
		for (int numeroFor = 1 ; numeroFor < 11 ; numeroFor++) {
			System.out.println(numeroFor);
		}
		
	}
}
