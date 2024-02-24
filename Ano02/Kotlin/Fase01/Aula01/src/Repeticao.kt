fun exRepeticao(){

    // if else
    val num = 10
    if (num == 10) {
    println("Número é 10")
    }
    else {
        println("Número não é 10")
    }

    // while
    var life = 10
    while (life > 0) {
        println("O jogador está com $life vidas")
        life -= 1
    }

    // for in
    // Percorrendo array
    var estudantes = arrayOf<String>("Marcela", "Mariana", "Matheus", "Marcos", "Melanie")
    for (estudante in estudantes){
        println(estudante)
    }


}