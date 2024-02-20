package br.com.fiap;

// CRIANDO UM OBJETO DA CLASSE CONTA

// classe principal
public class App {

	// sintaxe para classe principal
	public static void main (String[] args) {
		
		// tipo da variavel - classe ; nome - contaX ; sintaxe - new ; contrutor - nome da classe
		Conta contaX = new Conta();
		
		// contaX.nome = "Eduardo"; - Não é possível definir o nome pois esta como private esse atributo, para isso criamos o set nome que só nos retornará o nome
		contaX.setNome("Eduardo");

		// System.out.println(contaX.getNome());
		
		//outro objeto com os contrutores com parâmetros
		Conta contaY = new Conta("Jorge" , "123456" , "245");
		contaY.depositar(1000);
		
		System.out.println("Saldo = R$ " + contaY.getSaldo());
		
		contaY.sacar(500);
		
		System.out.println("Novo saldo = R$ " + contaY.getSaldo());
		
		System.out.println("Ola " + contaY.getNome() + " seu saldo é: R$ " + contaY.getSaldo());
	}
	
}
