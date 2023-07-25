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

*/
// --------------------------------------- //

arrayManipulacao = ['Notebook', 'Smarphone', 'Smartwatch', 'Tablet', 'Playstation 5']

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


console.log(arrayManipulacao)