import model.Funcionario
import model.Pessoa
import java.time.LocalDate

fun main() {
    // exArray()
    // exRepeticao()
    // exEnum()
    // exFuncao()

    val pessoa1 = Pessoa()
    pessoa1.nome = "Ana"
    pessoa1.altura = 1.75
    pessoa1.peso = 66
    pessoa1.dataNascimento = LocalDate.of(2001, 9, 21)

    pessoa1.exibirDados()

    // ------------ //

    val pessoa2 = Pessoa()
    pessoa2.nome = "João"
    pessoa2.altura = 1.84
    pessoa2.peso = 87
    pessoa2.dataNascimento = LocalDate.of(1987, 5, 6)

    pessoa2.exibirDados()

    // ---------- HERANÇA ---------- //

    var funcionario1 = Funcionario()
    funcionario1.nome = "José"
    funcionario1.peso = 90
    funcionario1.altura = 1.89
    funcionario1.cargo = "Desenvolvedor"
    funcionario1.salario = 9000.99

    funcionario1.exibirDados()


}