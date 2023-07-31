const data = document.querySelector('[data-JS]')
const dataAtual = new Date
const formatarData = Intl.DateTimeFormat('pt-BR', {dateStyle: 'long'})
data.textContent += formatarData.format(dataAtual)