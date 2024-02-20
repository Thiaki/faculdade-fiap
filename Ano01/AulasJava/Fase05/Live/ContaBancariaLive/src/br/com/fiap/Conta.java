// Definindo o pack em que esse código vai ficar
package br.com.fiap;

// Criando e definindo o nome da classe
public class Conta {	
	
	
	
	// definindp atributos
	// precisamos colocar o tipo de váriavel
	private String nome;
	private String numeroDaConta;
	private String agencia;
	private double saldo;
	
	
	// construtores padrão
	public Conta() {}
	
	// construtor com parâmetros
	public Conta(String nome, String numeroDaConta, String agencia) {
		this.nome = nome;
		this.numeroDaConta = numeroDaConta;
		this.agencia = agencia;
	}
	
	
	// definindo metodos
	// get - retorna um valor. Ex retornar nome
	public String getNome() {
		return nome;
	}
	
	public String getNumeroDaConta() {
		return numeroDaConta;
	}
	
	public double getSaldo() {
		return saldo;
	}
	
	public String getAgencia() {
		return agencia;
	}
	
	//set - retorna um objeto setando algum valor definido com parâmetros
	
	public void setNome(String nome) {
		// public void é utilizado quando não iremos mostrar nada ao usuário e só modificar atributos de um método
		this.nome = nome;
	}
	
	public void setnumeroDaConta(String numeroDaConta) {
		// this é para mostrar qual sera o atributo dessa classe que sera mudada, o que não estiver com o this, será o parâmetro
		this.numeroDaConta = numeroDaConta;
	}
	
	public void getAgencia(String agencia) {
		this.agencia = agencia;
	}
	
	
	
	// metodos das funcionalidades do sistema
	public void depositar (double valor) {
		saldo = saldo + valor;
	}
	
	public void sacar (double valor) {
		saldo = saldo - valor;
	}
	
	// 1 h 18 min
}
	
	