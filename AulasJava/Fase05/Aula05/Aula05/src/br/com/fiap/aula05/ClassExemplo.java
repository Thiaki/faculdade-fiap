package br.com.fiap.aula05;
import java.util.Scanner;
// Importando a classe que deixa possível o usuário digitar no programa

public class ClassExemplo {
	public static void main(String[] args) {
		System.out.print("Digite um número: ");
		Scanner sc = new Scanner(System.in);
		// Sintaxe para colocar a classe de inserir dados
		int numero = sc.nextInt();
		// Sintaxe para entrada de dados:
		// {tipo da variável} {variavel} = sc.next{tipo da variavel}()
		System.out.print("Seu número é: " + numero);
		sc.close();
	}
}
