package br.com.fiap.aula01;
import java.util.ArrayList;

public class ClassGeneric {

	public static void main(String args[]) {
		
		ArrayList<Cliente> listaCliente = new ArrayList<Cliente>();
		
		Cliente cliente01 = new Cliente();
		cliente01.setNome("Eduardo");
		
		Cliente cliente02 = new Cliente();
		cliente02.setNome("João");
		
		
		listaCliente.add(cliente01);
		listaCliente.add(cliente02);
		
		for (Cliente cliente : listaCliente) {
			System.out.println(cliente.getNome());
		}
		
		
	}
	
}
