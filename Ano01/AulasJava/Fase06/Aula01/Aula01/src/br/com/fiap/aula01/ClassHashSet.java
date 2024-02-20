package br.com.fiap.aula01;
import java.util.HashSet;

public class ClassHashSet {

	// PARECIDO COM ARRAYLIST, MAS NÃO É POSSÍVEL COLOCAR DOIS ELEMENTOS COM O MESMO NOME
	
	public static void main(String args[]) {
		
		HashSet linguagens = new HashSet<>();
		
		linguagens.add("Java");
		linguagens.add("Python");
		linguagens.add("JavaScript");
		
		linguagens.add("Java"); // Repetido, HashSet não deixa elementos repetidos
		
		System.out.print(linguagens);	
	}
	
}
