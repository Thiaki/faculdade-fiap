package br.com.fiap.aula01;

public class ClasseString {
	
	public static void main(String[] args) {
		
		String nome1 = "Fiap";
		String nome2 = "Fiap";
		
		// Comparar duas Strings
		if(nome1.equals(nome2)) {
			System.out.println("Strings iguais");
		}
		else {
			System.out.println("Strings diferentes");
		}
		
		
		// Comparar duas Strings para falso
		if(!nome1.equals(nome2)) {
			System.out.println("Strings diferentes");
		}
		else {
			System.out.println("Strings iguais");
		}
		
		
		// Comparar duas Strings desconsiderando as letras maiúsculas
		if(nome1.equalsIgnoreCase(nome2)) {
			System.out.println("Strings iguais");
		}
		else {
			System.out.println("Strings diferentes");
		}
		
		
		// Comparar Strings para ver se começam com o mesmo elemento
		String facu = "Fiap - A melhor faculdade de tecnologia";
		
		if(facu.startsWith("Fiap")){
			System.out.println("Começa com Fiap");
		}
		else {
			System.out.println("Não começa com Fiap");
		}
		
		
		// Comparar Strings para ver se terminam com o mesmo elemento
		if(facu.endsWith("gia")){
			System.out.println("Termina com gia");
		}
		else {
			System.out.println("Não termina com gia");
		}

		
		// Verifica o tamanho de uma String
		int caracteresFacu = facu.length();
		System.out.println("A string possui " + caracteresFacu + " caracteres");
		
		
		// Pega o elemento que está na posição descrita
		char caracterFacu = facu.charAt(0);
		System.out.println("O primeiro caracter da String é: " + caracterFacu);
		
		
		// Pega a posição do elemento descrito, se não tiver, retorna -1
		int posicao = facu.indexOf("faculdade");
		System.out.println("O elemento faculdade está na posição: " + posicao);
		
		
		// Mesma coisa do indexOf, mas pegando de trás para frente
		int posicaoContrario = facu.lastIndexOf("faculdade");
		System.out.println("O elemento faculdade está na posição: " + posicaoContrario);
		
		
		// Substring- pode colocar no parâmetro até dois valores, sendo o começo e o final da string que quer separar
		String novaString = facu.substring(16, 25);
		System.out.println("A string que começa no 16° índice e acaba no 25° da string facu é: " + novaString);
		
		
		// Transformar a String em maiúsculo ou minúsculo
		String maiusculo = facu.toUpperCase();
		System.out.println(maiusculo);
		String minusculo = facu.toLowerCase();
		System.out.println(minusculo);
		
		
		// Muda a parte da String pela outra selecionada
		String trocar = facu.replace("tecnologia", "São Paulo");
		System.out.println("Trocando a palavra Tecnologia, pour São Paulo: " + trocar);
		
		
		// Separa em um array a String pelo caracter determinado, nesse caso, o espaço
		String palavras[] = facu.split(" ");
		for (String marcador : palavras) {
			System.out.println(marcador);
		}
		
	}

}
