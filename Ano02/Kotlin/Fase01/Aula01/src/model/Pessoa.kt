package model

import java.time.LocalDate
import java.time.Period

// open faz com que essa classe (e métodos) permita que tenha herança
open class Pessoa {

    // Propriedades do objeto
    var nome: String = ""
    var dataNascimento: LocalDate = LocalDate.of(2000, 5, 10)
    var peso: Int = 0
    var altura: Double = 0.0

    // val idade pega o que esta no get (uma conta)
    val idade: Int
        get() {
            return Period.between(dataNascimento, LocalDate.now()).years
        }

    // Métodos: o que o objeto faz
    open fun exibirDados(){
        println("nome: $nome")
        println("Peso: $peso")
        println("Altura: $altura")
        println("Data de Nascimento: $dataNascimento")
        println("Idade: $idade")
        // println("Idade: ${calcularIdade()}")
        println("-------------------------------")
    }

//    fun calcularIdade(): Int{
//        var idade = Period.between(dataNascimento, LocalDate.now()).years
//        return idade
//    }

}