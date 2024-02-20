package br.com.fiap.aula05;
import java.io.*;

public class ExemploArquivo {
	public static void main(String[] args) {
		File arquivo = new File("arquivoteste.txt");
		// Verifica se o arquivo existe
		if (arquivo.exists()) {
			System.out.println("O arquivo existe!"+ "Pode ser lido: " + arquivo.canRead() + "Pode ser gravado: " + arquivo.canWrite() +"Tamanho: " + arquivo.length() + " Caminho: " + arquivo.getPath());
		} else {
			// Cria o arquivo
			try {
				if (arquivo.createNewFile())
					System.out.println("Arquivo criado!");
				else
	System.out.println("Arquivo não criado!");
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
