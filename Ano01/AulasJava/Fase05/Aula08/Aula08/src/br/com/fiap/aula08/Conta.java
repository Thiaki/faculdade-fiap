package br.com.fiap.aula08;

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
	
	// Métodos para setar agencia, numeroConta
	
	public int getAgencia() {
		return agencia;
	}
	
	public void setAgencia(int agencia) {
		this.agencia = agencia;
	}
	
	public int getNumeroConta() {
		return numeroConta;
	}
	
	public void setNumeroConta(int numeroConta) {
		this.numeroConta = numeroConta;
	}
	
	
	
	/*
	 * Acrescenta o valor no saldo da conta
	 * @param deposito que o usuário irá fazer
	 */
	public void depositar(double deposito) {
		saldo += deposito;
	}
	
	/*
	 * Tira o valor sacado
	 * @param valor sacado
	 */
	public void saque(double retirado) {
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
