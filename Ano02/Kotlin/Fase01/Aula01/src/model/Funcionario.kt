package model

class Funcionario: Pessoa() {

    var salario: Double = 0.0
    var cargo: String = ""

    // override faz com que a função exibirDados (que ja exite) seja setada essa quando for um objeto de Funcionário
    override fun exibirDados(){
        println("nome: $nome")
        println("Peso: $peso")
        println("Altura: $altura")
        println("Data de Nascimento: $dataNascimento")
        println("Idade: $idade")
        println("Salario: $salario")
        println("Cargo: $cargo")
        println("-------------------------------")
    }

}