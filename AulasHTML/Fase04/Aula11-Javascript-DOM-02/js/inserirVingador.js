const forms = document.querySelector('form')
// Colocando no form um escutador de quando o formulário for enviado
forms.addEventListener('submit', function(eventoSubmit) {
    // Cancelar o evento submit pois não esta enviando para nenhum lugar esse formulário
    eventoSubmit.preventDefault()

    // Procurando os campos de preenchimento do usuário
    const formVingadores = forms.querySelectorAll('input')

    // Atribuindo o novoVingador como uma array
    const novoVingador = [];


    formVingadores.forEach(campo => {
        // formVingadores seria todos os campos onde o usuário vai colocar sobre o herói novo
        // campo seria o nome de cada um, já que esta dentro de um forEach ele vai passar um de cada vez
        // campo.name é o nome de cada campo que ele vai passar
        // campo.value é o digitado pelo usuário

        // ESTA ATRIBUINDO O DIGITADO PELO USUÁRIO PARA O ARRAY NOVO VINGADOR COM OS NOMES DOS CAMPOS E OS VALORES DIGITADOS
        novoVingador[campo.name] = campo.value
    })
    novoVingador.xp = calcularXP(novoVingador.forca , novoVingador.agilidade , novoVingador.velocidade).toFixed(1)
    
    // Criando os elementos html
    const tr = document.createElement('tr')
    // Colocando as classes
    tr.classList.add('bg-success', "text-light")
    

    // Dado é o campo.name
    // in - se o dado estiver em novoVingador, ele entra no for
    for(let dado in novoVingador) {
        // Criando o elemento html
        const td = document.createElement('td')
        
        // Atribuindo o dado do array para o texto desse html
        td.textContent = novoVingador[dado]
        // Colocando o td dentro do tr
        tr.appendChild(td)
    }

    const tbody = document.querySelector('#vingadores')
    tbody.appendChild(tr)

    // Apagando o formulário
    this.reset()

})