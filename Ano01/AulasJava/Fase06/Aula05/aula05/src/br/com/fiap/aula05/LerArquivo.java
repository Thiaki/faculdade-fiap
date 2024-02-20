package br.com.fiap.aula05;
import java.io.*;

public class LerArquivo {
	public static void main(String args[]) {
		// tenta
		try {
			// abre o arquivo
			FileReader arquivo = new FileReader("arquivo.txt");
			BufferedReader ler = new BufferedReader(arquivo);
			
			// le uma linha do arquivo retornando a linha ou null
			String linha = ler.readLine();
			// verifica se a linha que esta lendo não existe (enquanto a linha for uma string ele printa e le a próxima linha)
			while (linha != null) {
				// escreve o que leu
				System.out.println(linha);
				// le a próxima linha do arquivo
				linha = ler.readLine();
			}
			ler.close();
			arquivo.close();
		}
		catch (IOException e){
			e.printStackTrace();
		}
	}
}
