// Definindo o pack em que esse código vai ficar
package br.com.fiap;

// Criando e definindo o nome da classe
public class Conta {	
	
	// atributos
	// precisamos colocar o tipo de váriavel
	public String nome;
	private String numeroDaConta;
	protected double saldo;
	String agencia;
	
	
	// metodos
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
	
	//set - retorna um objeto setando algum valor definido com parâmetros
	
	public void setNome(String nomeDoTitular) {
		nome = nomeDoTitular ;
	}
	//40:00
}
