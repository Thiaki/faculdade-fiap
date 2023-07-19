/*
// CAIXAS DE DIÁLOGO

alert("Alertando")
confirm("Confirmar alguma coisa")
prompt("Caixa de inserção de conteúdo")
*/





/*
// RETORNA VERDADEIRO OU FALSO

let num1 = parseFloat(prompt("Digite o primeiro número:"));
let num2 = parseFloat(prompt("Digite o segundo número:"));
let result = 0;

// Maior
result = (num1 > num2);
console.log("O", num1, "é maior que", num2,"? R:", result);

// Menor
result = (num1 < num2);
console.log("O", num1, "é menor que", num2,"? R:", result);

// Maior ou Igual
result = (num1 >= num2);
console.log("O", num1, "é maior ou igual que", num2,"? R:", result);

// Menor ou Igual
result = (num1 <= num2);
console.log("O", num1, "é menor ou igual que", num2,"? R:", result);

// Igual
result = (num1 == num2);
console.log("O", num1, "é igual que", num2,"? R:", result);

// Diferente
result = (num1 != num2);
console.log("O", num1, "é diferente que", num2,"? R:", result);

// Valores igual e do mesmo tipo (string, int, float...)
result = (num1 === num2);
console.log("O", num1, "é igual e do mesmo tipo que", num2,"? R:", result);

// Valores diferentes e de tipo diferente (string, int, float...)
result = (num1 !== num2);
console.log("O", num1, "é diferente e de tipo diferente que", num2,"? R:", result);
*/





/*
// FACILITANDO CONTAS

let valor = 100;

// Soma mais simples
valor += 10
console.log("A soma de 100 e 10 ficou =", valor)

// Subtração mais simples
valor -= 10
console.log("A subtração de 100 e 10 ficou =", valor)

// Multiplicação mais simples
valor *= 10
console.log("A multiplicação de 100 e 10 ficou =", valor)

// Divisão mais simples
valor /= 10
console.log("A divisão de 100 e 10 ficou =", valor)
*/





/*
//FUNÇÕES MATH

let valor = 10.11

// Retorna o próximo número inteiro 
console.log("Math.ceil", Math.ceil(valor))

// Retorna o anterior número inteiro 
console.log("Math.floor", Math.floor(valor))

// Retorna o número aproximado 
console.log("Math.round", Math.round(valor))

// Retorna o maior número 
console.log("Math.max", Math.max(10, 20, 30, 40, 50))

// Retorna o menor número 
console.log("Math.min", Math.min(10, 20, 30, 40, 50))

// Retorna a potência número (2 elevado a 5)
console.log("Math.pow", Math.pow(2, 5))

// Retorna um valor aleatório entre 0 e 1 
console.log("Math.random", Math.random())

// Retorna a raiz quadrada 
console.log("Math.sqrt", Math.sqrt(valor))

// Retorna a raiz cúbica 
console.log("Math.cbrt", Math.cbrt(valor))
*/




/*
// MÉTODOS DE STRING

let string = "Eduardo Thiaki"
let stringSobrenome = "Yoshida"

// Retorna a quantidade de caracteres
console.log(string.length)

// Retorna tudo em maiúsculo
console.log(string.toUpperCase())

// Retorna tudo em minúsculo
console.log(string.toLowerCase())

// Retorna qual o caracter que é dessa posição
console.log(string.charAt(10))

// Retorna a posição do caracter digitado
console.log(string.indexOf("a"))

// Retorna a posição do caracter digitado de trás para frente
console.log(string.lastIndexOf("a"))

// Concatena duas strings
console.log("".concat(string),"".concat(stringSobrenome))

// Substitui o primeiro termo pelo desejado
console.log(string.replace("a", "@"))

// Substitui todos os termos pelo desejado
console.log(string.replaceAll("a", "@"))

// Retorna a parte da string que definimos pelo numero do caracter
console.log(string.substring(8,14))

// Coloca em outra variavel uma parte da string
let novaString = string.slice(0,7);
console.log(novaString)

// Converte uma string em array
console.log(string.split(""))

// Remove os espaços em branco no começo e final da string
console.log(string.trim())

// Verifica se a string determinada tem dentro da outra string
console.log(string.includes("Edu"))

// Verifica se a string começa com o texto determinado
console.log(string.startsWith("Edua"))

// Verifica se a string termina com o texto determinado
console.log(string.endsWith("aki"))
*/




/*
// MÉTODO DE DATAS
const dataAtual = new Date()

console.log("A data atual é: ", dataAtual)

// Mostra o dia da semana
console.log(dataAtual.getDay() + 1)

// Mostra o dia do mês
console.log(dataAtual.getDate())

// Mostra o mês
console.log(dataAtual.getMonth() + 1)

// Mostra o ano
console.log(dataAtual.getFullYear())

// Mostra a hora
console.log(dataAtual.getHours())

// Mostra a minutos
console.log(dataAtual.getMinutes())

// Mostra a Segundos
console.log(dataAtual.getSeconds())
*/











// TREINANDO


/*
// Contas
let num1 = parseFloat(prompt("Digite o primeiro número:"));
let num2 = parseFloat(prompt("Digite o segundo número:"));
let result = 0;

// Soma
result = num1 + num2;
console.log("A soma de ", num1, "+", num2, "=", result);

// Subtração
result = num1 - num2;
console.log("A subtração de ", num1, "-", num2, "=", result);

// Multiplicação
result = num1 * num2;
console.log("A multiplicação de ", num1, "*", num2, "=", result);

// Divisão
result = num1 / num2;
console.log("A divisão de ", num1, "/", num2, "=", result);

// Módulo
result = num1 % num2;
console.log("O resto da divisão de ", num1, "e", num2, "é", result);

// Potência
result = num1 ** num2;
console.log("A potência de ", num1, "e", num2, "é", result);
*/