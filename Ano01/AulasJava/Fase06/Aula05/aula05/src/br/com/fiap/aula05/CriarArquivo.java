package br.com.fiap.aula05;
import java.io.*;

public class CriarArquivo {
	public static void main(String args[]) {
		// tenta
		try {
			// Abrir o arquivo
			FileWriter arquivo = new FileWriter("arquivo.txt");
			PrintWriter escrever = new PrintWriter(arquivo);
			
			// Escrever no arquivo
			escrever.println("Teste");
			escrever.println("Escrevendo no arquivo");
			escrever.println("Teste1");
			escrever.println("Teste2");
			escrever.println("Teste3");
			
			escrever.close();
			arquivo.close();
		}
		catch (IOException e) {
			e.printStackTrace();
		}
	}
}
