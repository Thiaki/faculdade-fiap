// FUNCTION
/*
Sintaxe
    function {nome-funcao}(parâmetros) {
        // Script da função
    }



// ------------------------------- //


// FUNCTION EXPRESS
// Serve para condensar funções
Sintaxe
    const {nome-funcao} = function(parâmetros) {
       // Script da função 
    }



// ------------------------------- //



// ARROW FUNCTION
// Serve para condensar funções
Sintaxe
    const {nome-funcao} = (parâmetros) => {
       // Script da função 
    }

*/






//TESTANDO

// TABUADA COM FUNÇÃO
function tabuada (numeroTab){
    console.log(`Estamos fazendo a tabuada do número ${numeroTab}`)
    for (let i =0 ; i <= 10 ; i++){
        let soma = numeroTab * i
        console.log(`${numeroTab} x ${i} = ${soma}`)
    }
    console.log("<-----Final da tabuada----->")
}

let numTabuada = prompt("Digite o numero da tabuada")
tabuada (numTabuada)




// FUNCÇÃO CALLBACK
function somar(x, y, z){
    return (x + y + z)
}

function subtrair(x, y, z){
    return (x - y - z)
}

function media(x, y, z){
    // toFixed(2) DEIXA 2 LINHAS DEPOIS DA VÍRGULA
    return ((x + y + z) / 3).toFixed(2)
}

function calcular(x, y, z, conta){
    return conta(x , y , z)
}
console.log(`A soma é ${calcular(10, 20, 20, somar)}`)
console.log(`A subtração é ${calcular(10, 20, 20, subtrair)}`)
console.log(`A media é ${calcular(10, 20, 20, media)}`)






// SENHA ALEATÓRIA DE 20 DIGITOS
const gerarSenha = () => {
    // Declarando os números da senha
    const caracteres = 'ABCDEFGHIJKLMNOPQRSUVWXYZabcdefghijklmnopqrsuvwxyz1234567890!@#$%&amp;*';
    let novaSenha = '';
    // Repetindo 20 vezes a escolha de caracteres
    for (let i = 0; i <= 19; i++) {
        // Colocando na variável indice a escolha aleatória pelo Math.random e depois multiplica pelos caracteres.length que calcula a quantidade de caracteres da variável, fazendo com que tenha o numero do caracter que será escolhido
        const indice = Math.round(Math.random() * caracteres.length);
        // Coloca na varivel novaSenha, a própria variável e acrescenta o caracter que esta dentro da variável caracter de indice da variável indice que foi caculado
        novaSenha += caracteres[indice];
    }
    return novaSenha;
}
console.log(`A senha gerada foi: ${gerarSenha()}`);