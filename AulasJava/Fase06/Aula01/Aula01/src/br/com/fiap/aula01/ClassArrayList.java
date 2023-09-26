package br.com.fiap.aula01;
import java.util.ArrayList;

public class ClassArrayList {

	public static void main(String args[]) {
		ArrayList linguagens = new ArrayList();
		
		// Adicionando "Java" no ArrayList
		linguagens.add("Java");
		
		// Subistitui o elemento no indice 0 (Java) para Python
		linguagens.set(0 , "Python");
		
		// Remove o elemento no indice 0
		linguagens.remove(0);
		
		
		linguagens.add("Java");
		linguagens.add("Python");
		
		
		// Printando o elemento de indice 1
		System.out.println(linguagens.get(1));
		System.out.println(" ");
		
		// Retorna o número de elementos de um ArraList
		int quantidade = linguagens.size();
		
		// Printando todos os elementos do ArrayList
		for (int i = 0 ; quantidade > i ; i++) {
			System.out.println(linguagens.get(i));
		}
		
		System.out.println(" ");
		
		// Retorna o indice do valor descrito (se tiver repetido, trás o primeiro)
		int indice = linguagens.indexOf("Python");
		System.out.println(indice);
		
		System.out.println(" ");
		
		// Parecido com o indexOf, mas trás o último valor
		int indiceContrario = linguagens.lastIndexOf("Java");
		System.out.println(indiceContrario);
		
		
	}
	
}
