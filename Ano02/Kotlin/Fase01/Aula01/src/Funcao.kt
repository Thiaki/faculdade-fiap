fun exFuncao(){
    /* Sintaxe Funções
     fun nomeDaFuncao(parâmetro: Tipo) : TipoDeRetorno {
        //Códigos
         return TipoDeRetorno
     }
    */

//    fun soma(a: Int, b: Int): Int {
//        return a + b
//    }
//
//    var result = soma(10, 15)
//    println(result)


    // ---------- MAP, FILTER, REDUCE ---------- //

    val numbers = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    // filter: filtrando pelos numeros pares (it é a variável temporária)
    var numerosPares = numbers.filter {it % 2 == 0}
    println(numerosPares)

    // map: passa individualmente por cada elemento do array e faz alguma operação
    var numerosMultiplicados = numbers.map { it * it }
    println(numerosMultiplicados)

    var sumNumbers = numbers.reduce {
        // acc é o número anterior que resultou a conta, nesse caso seria o acc + it
        // it é o número em ordem do array
        acc, it ->
        println("acc = $acc, it = $it")
        acc + it
    }
    println("Resultado da SOmatório: $sumNumbers")
}