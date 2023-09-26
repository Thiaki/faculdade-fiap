package br.com.fiap.aula08;

public class Main {
	public static void main(String[] args) {
		ContaCorrente cc = new ContaCorrente();
		cc.setAgencia(0001);
		cc.setNumeroConta(111222);
		cc.setTipo("PF");
		cc.setChequeEspecial(1234.00);		
	}
}
