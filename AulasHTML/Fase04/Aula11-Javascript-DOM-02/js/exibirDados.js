function exibirXP(){
    const vingador = document.querySelector('.vingador')
    vingador.forEach( heroi => {
        const forca = heroi.querySelector('.forca').textContent
        const velocidade = heroi.querySelector('.velocidade').textContent
        const agilidade = heroi.querySelector('.agilidade').textContent

        const resultadoXp = calcularXP(forca, agilidade, velocidade)

        heroi.querySelector('.xp-Final').textContent = resultadoXp.toFixed(1)
    })
}

dataHoje();
calcularXP();