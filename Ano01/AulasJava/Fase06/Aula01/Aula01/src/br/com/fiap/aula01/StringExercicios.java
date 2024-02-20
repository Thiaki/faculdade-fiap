package br.com.fiap.aula01;
import java.util.Scanner;

public class StringExercicios {

	public static void main(String[] args) {
		
		/* Exercício 01
		 * Considere a string ‘BANANADA’ e combine as instruções de manipulação de string para:
		 * Imprimir ANA, usando substr.
		 * Substituir a string ‘BANANADA’ por ‘BANDA’, usando a instrução delete. 
		 * Indicar as posições de todos os ‘A’s existentes na palavra ‘BANANADA’.
		 */
		
		/* Exercícío 02
		 * Indique se uma expressão é palíndroma.
		 * Exemplo: “AMOR” e “ROMA” não são palíndromos.
		 * “OVO” e “OVO” ou “AMOR ME AMA EM ROMA” e “AMOR ME AMA EM ROMA” são palíndromes.
		 */
		
		/* Exercício 03
		 * Leia atenciosamente a explicação sobre o CPF, em seguida, analise os algoritmos e elabore um programa em Java para implementá-lo.
		 * CÁLCULO DOS DÍGITOS DE CONTROLE DO CPF
		 * O cálculo dos dígitos de controle do CPF é um algoritmo bem interessante para apresentação das técnicas associadas aos comandos de manipulação de conjuntos de caracteres ou strings. No caso do CPF, são válidos os seguintes aspectos:
		 * O CPF possui 11 dígitos; os dois últimos números são dígitos de controle.
		 * O primeiro dígito de controle é calculado com base nos 9 primeiros dígitos.
		 * O segundo dígito de controle é calculado com base nos 9 primeiros dígitos e no primeiro dígito de controle.
		 * A Região Fiscal onde é emitido o CPF (definida pelo nono dígito) tem a seguinte abrangência: 1 (DF-GO-MS-MT-TO), 2 (AC-AM-AP-PA-RO-RR), 3 (CE-MA-PI), 4 (AL-PB-PE-RN), 5 (BA-SE), 6 (MG), 7 (ES-RJ), 8 (SP), 9 (PR-SC) e 0 (RS).
		 */
		
		
		// ---------------------------------- //
		
		
		Scanner sc = new Scanner(System.in);
		
		// Exercício 1
		/*
		// A
		String bananada = "Bananada";
		String novaAna = (bananada.substring(3, 6));
		System.out.println(novaAna.toUpperCase());
		
		// B
		String novaBanda = bananada.replace("nana", "n");
		System.out.println(novaBanda);
		
		// C
		for (int cont = 0 ; cont < bananada.length() ; cont++) {
			char stringA = bananada.charAt(cont);
			if (stringA == 'a') {
				System.out.print(cont + " ");
			}
		}
		System.out.println(" ");
		*/
		
		// ---------------------------------- //
		
		
		// Exercício 2
		/*
		System.out.print("Digite a frase para saber se ela é palíndroma: ");
		String stringPalindroma = sc.nextLine();
		stringPalindroma = stringPalindroma.replaceAll(" ", "");
		
		StringBuilder stringPalindromaReverse = new StringBuilder(stringPalindroma).reverse();
		
		String stringConvertida = stringPalindromaReverse.toString();
		
		if (stringPalindroma.equalsIgnoreCase(stringConvertida)) {
			System.out.println("Strings Palíndroma");
		} else {
			System.out.println("Strings Não Palíndroma");
		}
		 */
		
		// ---------------------------------- //
		
		
		// Exercício 03
		System.out.print("Digite o CPF para descobrir os últimos dois dígitos: ");
		String cpf = sc.nextLine();
		
		int digitos[] = new int[cpf.length()];
		
		for (int i = 0 ; i < cpf.length() ; i++) {			
			int a = digitos[i];
			System.out.println(a);
		}
	}
	
}
