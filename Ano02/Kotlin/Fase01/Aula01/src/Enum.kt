// Enum é criado quando queremos um tipo comum e um conjunto fechado de valores
enum class Compass {
    norte,
    leste,
    sul,
    oeste
}

// ------ Valores Padrões ------ //

enum class SeatPosition(var seat: String){
    aisle("corredor"),
    middle("meio"),
    window("janela")
}

fun exEnum(){
    var direction = Compass.norte

    when (direction) {
        Compass.norte ->
            println("Estamos indo para norte")

        Compass.sul ->
            println("Estamos indo para sul")

        Compass.leste ->
            println("Estamos indo para leste")

        Compass.oeste ->
            println("Estamos indo para oeste")
    }

    // ------ Valores Padrões ------ //

    // Definindo valor padrão
    var passangetSeat = SeatPosition.middle

    // Buscando o valor padrão
    println(passangetSeat.seat)
}