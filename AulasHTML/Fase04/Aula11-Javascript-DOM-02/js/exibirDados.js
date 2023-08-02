function exibirXP() {
    // Colocando a variavel vingador todas as linhas com os vingadores e seus atributos
    const vingador = document.querySelectorAll('.vingador')
    // Passando por todos os vingadores um de cada vez
    vingador.forEach(heroi => {
        // Procurando os atributos de cada um separadamente
        const forca = heroi.querySelector('.forca').textContent
        const velocidade = heroi.querySelector('.velocidade').textContent
        const agilidade = heroi.querySelector('.agilidade').textContent

        // Fazendo a conta do seu XP
        const resultadoXp = calcularXP(forca, agilidade, velocidade)

        // Procurando o texto da classe xp-Final e atribuindo o valor que fizemos a conta 
        heroi.querySelector('.xp-Final').textContent = resultadoXp.toFixed(1)
    })
}

// Exibindo as duas funções
exibirXP();
dataHoje();