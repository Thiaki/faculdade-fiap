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
blur - algum elemento perde o foco
*/





// ---------------------------------------------------- //





// CALCULANDO XP DOS HERÓIS E COLOCANDO COR NOS ELEMENTOS

// Achando o botão que executará a função
const botaoCalcular = document.querySelector('#calcular')
// Colocar a função no click do botão com uma arrow function sem parâmetros e sem nome
botaoCalcular.addEventListener('click', () => {
    // Achando a as linhas com os nomes e atributos de todos os vingadores (querySelectorAll)
    const vingadores = document.querySelectorAll('.vingador')
    // For Each para passar por todos as linhas dos arrays separadamente, pois quando é feito o querySelectorAll, todos os elementos viram diferentes elementos de um array
    vingadores.forEach(vingadorQueEstamosVendoAgora => {
        // Achando e transformando em Number o texto (textContent) dentro da classe'forca' de uma das linhas (ja que esta dentro do forEach)]
        // NÃO COLOCA DOCUMENT.QUERYSELECTOR PORQUE ESTAMOS PROCURANDO DENTRO DE CADA VINGADOR, E NÃO DO DOCUMENTO INTEIRO
        const forca = Number(vingadorQueEstamosVendoAgora.querySelector('.forca').textContent)
        const velocidade = Number(vingadorQueEstamosVendoAgora.querySelector('.velocidade').textContent)
        const agilidade = Number(vingadorQueEstamosVendoAgora.querySelector('.agilidade').textContent)
        const xp = (forca + velocidade + agilidade) / 3
        // Achando o texto (textContent) do elemento em que vamos colocar o xp do vingador que esta na classe xp-Final
        vingadorQueEstamosVendoAgora.querySelector('.xp-Final').textContent = xp.toFixed(1)
        // Adicionando as classes no elemento vingador se o xp <= 91
        if(xp <= 91) {
            vingadorQueEstamosVendoAgora.classList.add('bg-danger', 'text-light')
        }
    })
})