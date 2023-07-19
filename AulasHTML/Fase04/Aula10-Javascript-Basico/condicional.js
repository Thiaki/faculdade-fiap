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
    
    
    // -------------------------------- //
    
    
// FOR
// Estrutura de repetição para quando sabemos a quantidade exata de repetições
    
    Sintaxe

    for ( {variavel} = {valor-inicial} ; {variavel} < {valor-final} ; {variavel}++ ){
        // Inicia quando a variavel for igual ao valor-inicial e termina quando a variavel for igual ao valor-final e sempre incrementando a variavel com ++
    }
    

    // -------------------------------- //
    
    
// WHILE
// Estrutura de repetição para quando geralmente não sabemos a quantidade exata de repetições
    
    Sintaxe

    while ( {variavel} = {valor} ) {
        // Quando a variavel for igual ao valor
    }
    

    // -------------------------------- //
    
    
// DO / WHILE
// Estrutura de repetição que sempre rodará pelo menos uma vez o código para depois ver a condição
    
    Sintaxe

    do {
        // Bloco que será repetido pelo menos uma vez
    }

    while ( {condição} )
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


// UTILIZANDO IF E ELSE ENCADEADO
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


// UTILIZANDO FOR IF

let par = 0
let impar = 0
let soma = 0

for (let i = 1 ; i < 11 ; i++){
    let numAleatorio = Math.round((Math.random() * 100))
    console.log(`O ${i} numero aleatório é ${numAleatorio}`)
    soma = soma + numAleatorio
    if (numAleatorio % 2 == 0){
        par = par + 1
    }
    else{
        impar = impar + 1
    }
}

console.log(`Deles, temos ${par} par(es) e ${impar} impar(es)`)
console.log(`A soma deles é de ${soma}`)


// UTILIZANDO WHILE FOR IF

let numAleatorio;
let totalSorteio = 10;

for (let i = 0; i <= 9; i++) {
    
    numAleatorio = Math.round(Math.random() * 100);
    
    while(numAleatorio % 2 !== 0)
    {
        numAleatorio = Math.round(Math.random() * 100);
        totalSorteio++;        
    }
    
    console.log(`Números sorteados: ${numAleatorio}`);
}

console.log(`Quantidade de sorteios realizados: ${totalSorteio}`);


// UTILIZANDO DO / WHILE

let numero = 10

do {
    console.log(numero)
    numero--
}
while (numero >= 0)

console.log("Final da conta")