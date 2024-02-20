package br.com.fiap.aula06;

public class Conta {
	private int numeroConta;
	private int agencia;
	private double saldo;
	
	// Métodos
	
	public Conta() {
		
	}
	
	public Conta (int numeroConta, int agencia, double saldo) {
		this.numeroConta = numeroConta;
		this.agencia = agencia;
		this.saldo = saldo;
	}
	
	/*
	 * Acrescenta o valor no saldo da conta
	 * @param deposito que o usuário irá fazer
	 */
	public void setDepositar(double deposito) {
		saldo += deposito;
	}
	
	/*
	 * Tira o valor sacado
	 * @param valor sacado
	 */
	public void setSaque(double retirado) {
		saldo -= retirado;
	}
	
	/*
	 * Verifica o saldo
	 * @return saldo da conta
	 */
	public double getVerificarSaldo() {
		return saldo;
}
}
