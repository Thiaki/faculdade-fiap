
/*
// Retorna o primeiro achado no documento
Sintaxe
    document.querySelector(#id-elemento)

Retorna todos do documento
Sintaxe
    document.querySelectorAll(.class-elemento)

// ------------------------------- //

// Cria um elemento html
Sintaxe
    createElement(tag-html)

// ------------------------------- //

// Adiciona um escutador de eventos html.   Ex. o clique do usuário
Sintaxe
    addEventListener(evento-clique)

// ------------------------------- //

// Adiciona ou remove um filho ao elemento html
Sintaxe Adicionar
    apeendChild(elemento-adicionar)
Sintaxe Remover
    removeChild(elemento-remover)

// ------------------------------- //

// Adiciona, retorna ou remove um atributo ao elemento html
Sintaxe Adicionar
    setAttribute(atributo-adicionar)
Sintaxe Retorna
    getAttribute(atributo-retornar)
Sintaxe Remove
    removeAttribute(atributo-remove)

// ------------------------------- //

// Clona algum elemento html
Sintaxe
cloneNode(elemento-clonado)

// ------------------------------- //

// Adiciona classe ao elemento html
Sintaxe
    elemento.classList.add('class01', 'class02')
*/




// ---------------------------------------------------- //





let atributos = document.querySelectorAll('td')
console.log(atributos)
// textContent faz pegar somente o texto do elemento html
atributos[5].textContent = 'Homem Aranha'


// No seguinte código vamos colocar a data que atualizamos em "Dados atualizados: "
// Esse elemento esta com um data que utilizamos exclusivamente para o javascript do elemento
const dataAtualizacao = document.querySelector("[data-JS]")
// Pegando a data atual
const dataAtual = new Date()
// Formatando a data para brasileira e o tamanho dela
const formatadaData = Intl.DateTimeFormat('pr-BR',{dateStyle: "short"})
// Vendo o texto da variável dataAtualização e substituindo pela formatação que fizemos na variavel dataAtual
dataAtualizacao.textContent = (`Dados Atualizados: ${formatadaData.format(dataAtual)}`)





// ---------------------------------------------------- //





//EVENTOS
/*
Possuem duas formas de serem aplicados:
1. document.querySelector('elemento=html').onclick = function
2. document.querySelector('elemento-html').addEventListener('click', function)

click - quando o elemento é clicado
dblclick - quando é clicado duas vezes
mouseover - mouse em cima do elemento
mouseup - mouse sai do elemento
keydown - uma tecla esta pressionada
keyup - uma tecla deixa de ser pressionada
load - algum objeto for carregado
scroll - acontece scroll em algum elemento
submit - o formulário foi enviado
reset - o formulário foi resetado
change - o valor de algum elemento dor modificado
focus - algum elemento ganha foco
blu - algum elemento perde o foco
*/