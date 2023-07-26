/*
const arrayExemplo = ['Aluno', 'Planta', 'Diretor', 'Coordenador']

// MODIFICANDO O SEGUNDO ELEMENTO DA ARRAY
arrayExemplo[1] = 'Professor'

// QUANTIDADE DE ELEMENTOS DENTRO DE UMA ARRAY
arrayExemplo.length

// INSERIR UM NOVO CONTEÚDO NA PRIMEIRO ÍNDICE
arrayExemplo.unshift('Primeiro')

// INSERIR UM NOVO CONTEÚDO NO ÚLTIMO ÍNDICE
arrayExemplo.push('Último')

// REMOVE O PRIMEIRO ÍNDICE
arrayExemplo.shift()

// REMOVE O ÚLTIMO ÍNDICE
arrayExemplo.pop()

// EXCLUI OU INSERE UM ELEMENTO EM UM ÍNDICE ESPECÍFICO.
// Primeiro valor é o qual vai começar esse argumento / Segundo é qual índice será apagado / Terceiro é qual elemento será adicionado no ídice que foi demaracado no primeiro valor
arrayExemplo.splice(1, 0, 'Teste')

// MOSTRA O QUE DEVE SER EXIBIDO, O PRIMEIRO VALOR É O ÍNDICE DE O SEGUNDO O ÍNDICE DE FIM 
arrayExemplo.slice(0, 1)

// MOSTRA O ÍNDICE DO PRIMEIRO VALOR ENCONTRADO
arrayExemplo.indexOf('Aluno')

// MOSTRA O ÍNDICE DO ÚLTIMO VALOR ENCONTRADO
arrayExemplo.lastIndexOf('Aluno')

// JUNTA DOIS ARRAYS, CRIANDO UM NOVO ARRAY
array01 = ['a', 'b', 'c']
arrayConcat = arrayExemplo.concat(array01)

// COLOCA OS ELEMENTOS EM ORDEM ALFABÉTICA
arrayExemplo.sort()

// INVERTE OS ELEMENTOS DA ARRAY
arrayExemplo.reverse()

// TRANSFORMA A ARRAY EM UMA STRING E É POSSÍVEL COLOCAR UM SEPARADOR ENTRE ELES
arrayExemplo.join('-')

// Retorna com true ou false se o elemento está presente na array
arrayExemplo.includes('Teste')


console.table(arrayExemplo)


// --------------------------------------- //


arrayManipulacao = ['Notebook', 'Smartphone', 'Smartwatch', 'Tablet', 'Playstation 5']

// EVERY() TEM COMO OBJETIVO MOSTRAR PARA GENTE SE TODOS OS ELEMENTOS DA ARRAY TEM UMA DETERMINADA CONDIÇÃO
// Colocando na variável possuiLetraA o retorno true ou false
let possuiLetraA = arrayManipulacao.every(
    // Criando uma função para verificar se todos os elementos possuem a letra A
    // produto seria onde cada elemento do array passa, default o every verifica cada elemento da array
    produto => {
    return produto.includes('a');
}
)



// SOME() VERIFICA SE PELO MENOS 1 ELEMENTO DA ARRAY TEM UMA DETERMINADA CONDIÇÃO
// Colocando na variável maxCaracteres10 o retorno true ou false
const maxCaracteres10 = arrayManipulacao.some(
    // Criando uma função para verificar se dentro da array tem algum elemento mais que 10 caracteres
    // produto seria onde cada elemento do array passa, default o some verifica cada elemento da array
    produto => {
        return produto.length <= 10;
    }
)



// FIND() RETORNA O PRIMEIRO ELEMENTO QUE ESTA DENTRO DA CONDIÇÃO DETERMINADA
const possuiLetraO = arrayManipulacao.find(
    produto => {
        return produto.includes('o')
    }
) 


// --------------------------------------- //


arrayString = ['Notebook', 'Smartphone', 'Smartwatch', 'Tablet', 'Playstation 5']
arrayNumber = [100, 200, 300, 500, 600, 700, 800, 1000, 1100, 1300]

// FILTER() RETORNA UM NOVO ARRAY COM OS VALORES QUE SATISFAZEM A CONDIÇÃO DEFINIDA
// Esta colocando dentro da variável palavra todos os produtos que possuem Smart
const palavra = arrayString.filter(produto => {
    return produto.includes('Smart')
})
console.log(palavra)

const maiorValor = arrayNumber.filter(valor => {
    return valor > 500
})
console.log(maiorValor)



// MAP() APLICA UMA FUNÇÃO EM CADA ELEMENTO DO ARRAY E RETORNA UM NOVO PARA TODO ELEMENTO QUE SATISFAÇA
// Colocando dentro da variável letraMaiuscula todos os elementos em maiúsculo
const letraMaiuscula = arrayString.map(produto => {
    // Colocando todas as strings em maiúsculo
    return produto.toUpperCase()
})
console.log(letraMaiuscula)

// Coloca na variável desconto todos os elementos com um desconto de 10%
const desconto = arrayNumber.map(valor => {
    // Coloca todas os numbers -10%
    return valor - (valor * 0.1)
})
console.log(desconto)



// REDUCE() APLICA UMA FUNÇÃO EM CADA ELEMENTO DO ARRAY E RETORNA APENAS UM VALOR
// Coloca na variável totalValores a soma de todos os valores da array.
// Define o "acumulador" que vai juntar os valores e o "valor" que é cada elemento da array
const totalValores = arrayNumber.reduce((acumulador, valor) => {
    // Retorna o "acumulador" somado a todos os elementos.
    return acumulador + valor
// Definindo o "acumulador" em 0
}, 0)
console.log(totalValores)

*/
// --------------------------------------- //


const arrayProdutos = ['Smartphone', 'Notebook', 'Smartwatch', 'Tablet', 'Teclado', 'Mouse', 'Caixa de som', 'Fone de ouvido', 'Webcam', 'Roteador' ]

// UTILIZANDO O FOR PARA VERIFICAR NOSSOS ELEMENTOS EDNTRO DO ARRAY
// Definindo o contador (i) e o array lenght para verifica a quantidade de vezes que o for será feito
for(let i = 0; i < (arrayProdutos.length); i++) {
    // Exibindo o elemento i (ex: primeiro 1 , segundo 2 ...) do array arrayProdutos
    console.log(`Indice ${i} do array é: ${arrayProdutos[i]}`)
}

console.log("<------------------------------>")

// UTILIZANDO O FOR IN PARA VISUALIZAR TODOS OS ELEMENTOS
// Com o for in ele automaticamente ve quantos elemento o array possui e roda ele inteiro, sem precisar colocar o i++ e nem a contagem dos elementos do array
for (let i in arrayProdutos) {
    console.log(`Indice ${i} do array é: ${arrayProdutos[i]}`)
}

console.log("<------------------------------>")

// UTILIZANDO O FOR OFF PARA DEIXAR OS ELEMENTOS DO ARRAY EM MAIÚSCULO
// O for off despreza o indice e checa os elementos do array
for (let elemento of arrayProdutos) {
    console.log(elemento.toUpperCase())
}

console.log("<------------------------------>")

// FOT EACH APLICA UMA FUNÇÃO PARA CADA INDICE DOS ELEMENTOS DE UMA ARRAY
let maiorCaracter = 0

// Depois do for each esta colocando uma funcao com o parametro produto que vai guardar todos os elementos do array um de cada vez, fazendo com que passe pela função um array de cada vez 
arrayProdutos.forEach( produto => {
    console.log(`${produto} possui ${produto.length} caracteres`)
    // Fazendo um if para descobrir qual o produto com mais caracteres
    if (produto.length > maiorCaracter){
        maiorCaracter = produto.length
        maiorProduto = produto
    }
})

console.log(`O ${maiorProduto} possui mais caracteres, com ${maiorCaracter} caracteres`)