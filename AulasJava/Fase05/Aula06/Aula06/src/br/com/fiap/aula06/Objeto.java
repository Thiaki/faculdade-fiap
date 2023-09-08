package br.com.fiap.aula06;

public class Objeto {
	public static void main(String[] args) {
		// Conta (numeroConta, agencia, saldo)
		
		Conta poupanca = new Conta();
		
		System.out.println(poupanca.getVerificarSaldo());
		
		poupanca.setDepositar(1000.00);
		
		System.out.println(poupanca.getVerificarSaldo());
		
		poupanca.setSaque(412.80);
		
		System.out.println(poupanca.getVerificarSaldo());
	}
}
