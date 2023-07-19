// IF ELSE
/*
Sintaxe
    if (teste-lógico){
        //TRUE
    }

    else{
        //FALSE
    }



// ------------------------------- //


// IF TERNÁRIO
// Coloca em uma variável true ou false com um condicional pequeno

Sintaxe
    const {variavel} = ( {variavel} = 0 ? "Sim" : "Não" )


// -------------------------------- //


// SWITCH
// Parecido com um if encadeado, mas ele define blocos a serem executados se o valor foi exato

Sintaxe
    switch ( {variavel} ) {
        case {valor01}:
            // Se a variavel for igual ao valor 01
            break;
        case {valor02}:
            // Se a variavel for igual ao valor 02
            break;
        case {valor03}:
            // Se a variavel for igual ao valor 03
            break
        default:
            // Caso nenhum dos eventos ocorra
    }  
*/




// TESTANDO

// VERIFICAR SE O NÚMERO É PAR OU ÍMPAR
let numAleatorio = Math.round(Math.random() * 50)

if (numAleatorio % 2 == 0){
    console.log(`${numAleatorio} é um número PAR`)
}

else{
    console.log(`${numAleatorio} é um número ÍMPAR`)
}


// VERIFICANDO QUAL NÚMERO É MAIOR QUE O OUTRO
let numSorteado1 = Math.round(Math.random() * 50);
let numSorteado2 = Math.round(Math.random() * 50);
console.log(`Números sorteados: ${numSorteado1} e ${numSorteado2}`);
if (numSorteado1 > numSorteado2) {
    console.log(`O número ${numSorteado1} é maior que o número ${numSorteado2}`);
}
else if (numSorteado2 > numSorteado1) {
    console.log(`O número ${numSorteado2} é maior que o número ${numSorteado1}`);
}
else {
    console.log(`${numSorteado1} é igual ao número ${numSorteado2}`);
}


// UTILIZANDO IF TERNÁRIO
let valor = 0
const cond = (valor == 1 ? "Sim" : "Não")
console.log(cond)