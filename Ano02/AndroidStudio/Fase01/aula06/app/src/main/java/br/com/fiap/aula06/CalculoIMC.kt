package br.com.fiap.aula06

import kotlin.math.pow

fun calcularImc(altura: Double, peso: Double) : Double {
    return peso / (altura / 100).pow(2.0)
}

fun classificacaoImc(imc : Double): String {
   var situacao = ""
    if(imc < 18.5) {
        situacao = "Abaixo do peso"
    } else if (imc >= 18.5 && imc < 25.0) {
        situacao = "Peso Ideal"
    } else if (imc >= 25.0 && imc < 30.0) {
        situacao = "Levemente acima do peso"
    } else if (imc >= 30.0 && imc < 35.0) {
        situacao = "Obesidade Grau I"
    } else if (imc >= 35.0 && imc < 40.0) {
        situacao = "Obesidade Grau II"
    } else {
        situacao = "Obesidade Grau III"
    }
    return situacao
}