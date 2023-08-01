// const forms = document.querySelector('form')
// forms.addEventListener('submit', function(eventoSubmit) {
//     // Cancelar o evento submit pois não esta enviando para nenhum lugar esse formulário
//     eventoSubmit.preventDefault()
//     const formVingadores = forms.querySelector('input')
//     const novoVingador = {};
//     formVingadores.forEach(campo => {
//         novoVingador[campo.name] = campo.value
//     })
//     novoVingador.xp = calcularXP(novoVingador.forca , novoVingador.agilidade , novoVingador.velocidade).toFixed(1)
    
//     const tr = document.createElement('tr')
//     tr.classList.add('bg-secondary', "text-light")
    
//     for(let dado in novoVingador) {
//         const td = document.createElement(td)
        
//         td.textContent = novoVingador[dado]
//         tr.appendChild(td)
//     }
//     const tbody = document.querySelector('#vingadores')
//     tbody.appendChild(tr)

//     this.reset()

// })




const tbody = document.querySelector('tbody')

document.querySelector('form').addEventListener('submit', function(eventoSubmit) {
    eventoSubmit.preventDefault();

    const novoVingador = [
        document.querySelector('#nome'),
        document.querySelector('#forca'),
        document.querySelector('#velocidade'),
        document.querySelector('#agilidade'),
    ]

    const tr = document.createElement('tr')
    tr.classList.add('vingador', 'bg-secondary', "text-light")

    // Para cada campo que criamos (nome, forca, agilidade, velocidade) é criado uma td diferente e todas ficam dentro de um mesmo tr que foi criado anteriormente
    novoVingador.forEach(campo => {
        const td = document.createElement('td')
        td.textContent = campo.value
        tr.appendChild(td)
    })

    tbody.appendChild(tr)

    this.reset()
})