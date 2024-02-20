 // Criando objetos
const produto1 = {
    id: 1,
    tipo: 'Celular',
    fabricante: 'Apple',
    preco: 4899.00,
}

const produto2 = {
    id: 2,
    tipo: 'Notebook',
    fabricante: 'Asus',
    preco: 6899.00,
}


// Exibir apenas uma das suas propriedades
console.log(produto1.tipo)
console.log(produto2.preco)

// Inserir outra propriedade
produto1.propriedadeExemplo = 'abcdef'
console.log(produto1)

// Deletar outra propriedade
delete produto1.propriedadeExemplo
console.log(produto1)




// MÉTODO CONSTRUTOR
// Constroi um objeto automaticamente dado os valores
function produtoConstrutor(id, tipo, fabricante, preco) {
    this.id = id
    this.tipo = tipo
    this.fabricante = fabricante
    this.preco = preco
}
const produto3 = new produtoConstrutor(3, 'Celular', 'Samsung', 1699.00)



// FABRICA DE FUNÇÕES
// Fabrica um objeto utilizando o return e para declara o valores não precisa do 'this'
function produtoFuncao(id, tipo, fabricante, preco) {
    return {
        id,
        tipo,
        fabricante,
        preco,
    }
}
const produto4 = produtoFuncao(4, 'Processador', 'Intel', 1800.00)
console.log(produto4)



// ADICIONAR MÉTODOS
function produtoMetodo(id, tipo, fabricante, preco) {
    return {
        id,
        tipo,
        fabricante,
        preco,
        // Definindo a função dentro do objeto
        exibir: function () {
            console.log(id)
            console.log(tipo)
            console.log(fabricante)
            console.log(preco)
        }
    }
}
const produto5 = produtoMetodo(5, 'Tablet', 'LG', 1200.00)

// Exibindo tudo
console.log(produto5)

// Exibindo apenas a função
produto5.exibir()



// ---------------------------//



// SPREAD elementos de um objeto ou uma array sejam repassados a outra, como se estivessem sido duplicados, concatenados ou inserir mais parâmetros
/*
Sintaxe Array
    const {novo-array} = [...{array-um}...{array-dois}]
Sintaxe Objeto
    const {novo-objeto} = {...{objeto-um}, propriedade-nova: valor-nova}
*/
const produto6 = produtoFuncao(6, 'Notebook', 'Positivo', 4500.00)
const produto6Upgrade = {...produto6, modelo: 123}
console.log(produto6Upgrade)



// REST com ele é possível colocar "infinitos" argumentos dentro da array
/*
Sintaxe
    function {nome-função}(...{argumentos}) {
        // Função com os infinitos argumentos
    }
*/
// Parâmetro numero será todos os numeros que será definido
function somar(...numero){
    let total = 0
    // Para cada elemento da função será feito essa arrow funtion, somar o numero no total que inicialmente é 0
    numero.forEach(numero => {
        total = total + numero
    })
    return total
}



// DESESTRUTRAÇÃO podemos separar os elementos de um array ou objeto em diferentes variáveis
/*
Sintaxe Array
    const [variavel1, variavel2] = array
Sintaxe Objeto
    const {variavel1, variavel2} = objeto
*/
const prod = ['Celular', 'Tablet', 'Smartphone', 'Televisão']
// Colocando 'Celular' em prod1 ...
const [prod1, prod2, ...outrosProdutos] = prod
console.log(prod1)








// TESTANDO

// Rest
function media(...numeros) {
    let totalSoma = 0
    let totalNumeros = 0
    numeros.forEach(numero => {
        totalSoma = totalSoma + numero
        totalNumeros = totalNumeros + 1
    })
    return (totalSoma / totalNumeros).toFixed(2)
}
console.log(media())