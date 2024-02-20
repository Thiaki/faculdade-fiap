package br.com.fiap.aula08;

// Sintaxe de ContaCorrente ter a herança de Conta
public class ContaCorrente extends Conta {
	
	// Criando novos atributos apenas de conta corrente
	private String tipo;
	private double chequeEspecial;
	
	
	public String getTipo() {
		return tipo;
	}
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	public double getChequeEspecial() {
		return chequeEspecial;
	}
	public void setChequeEspecial(double chequeEspecial) {
		this.chequeEspecial = chequeEspecial;
	}
	
	public double getSaldoDisponivel() {
		// super. faz com que traga um método da classe maior
		return super.getVerificarSaldo() + chequeEspecial;
	}
	
	
	// Esse método foi criado com o mesmo nome da superclassse, então para n~çao ter conflito devemos fazer o @Override que sobrescreve esse méetodo da superclasse
	@Override
	public void saque(double valor) {
		// Adicionando a taxa de 10 reais
		valor += 10;
		super.saque(valor);
	}
	
}
