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


console.log(arrayExemplo)