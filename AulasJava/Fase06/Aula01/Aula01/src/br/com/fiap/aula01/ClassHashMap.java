package br.com.fiap.aula01;
import java.util.HashMap;

public class ClassHashMap {

	// PARECIDO COM HASHSET, MAS COLOCAMOS DOIS ELEMENTOS, UM COMO ID E OUTRO COMO VALOR PARA FACILITAR A BUSCA
	
	public static void main(String args[]) {
		HashMap alunos = new HashMap();
		
		
		// put - Adiciona um valor
		alunos.put("RM1234", "João");
		alunos.put("RM5678", "Maria");
		
		// get - Puxa o valor com o id
		System.out.println(alunos.get("RM1234"));
		
		// remove - Remove um elemento
		alunos.remove("RM1234");
		
		
		System.out.println(alunos);
		
	}
	
}
