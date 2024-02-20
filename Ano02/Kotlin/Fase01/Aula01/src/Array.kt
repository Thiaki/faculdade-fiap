import kotlin.io.path.fileVisitor

fun exArray(){

    // var {nome-variavel} = {valor}
    // val {nome-constante} = {valor}


    // -------------------------- //


    // Não é possível misturar tipos de dados diferentes nas coleções
    var cidades = arrayListOf<String>("São Paulo", "Rio de Janeiro", "Curitiba")
    println(cidades[2])

    cidades[2] = "Florianópolis"
    println(cidades[2])

    // Manipulação de Array

    // Verificar se Array esta vazio
    val arrayVazia = cidades.isEmpty() //Retorna true ou false

    // Quantidade de itens no Array
    val arrayTamanho = cidades.size

    // Adicionar item no Array
    cidades.add("Guarulhos")

    // Consultar no Array
    cidades.contains("São Paulo") // Retorna true ou false

    // Remove algum item no Array
    cidades.remove("São Paulo")


    // -------------------------- //


    // HashSet faz com que não seja possível ter elementos iguais no Array
    var filmes = HashSet<String>();
    filmes.add("Homem Aranha")
    filmes.add("Senhor dos Anéis")

    // Não adiciona elementos iguais
    filmes.add("Homem Aranha")
    println(filmes)


    // -------------------------- //


    // Map é possível colocar chave e valor
    var produtos = HashMap<String, Double>()

    // Adicionando elementos
    produtos.put("Mouse", 49.99)
    produtos.put("Teclado", 149.99)
    produtos.put("Monitor", 799.99)

    // Passa a chave no get e ele retorna o avlor
    println(produtos.get("Monitor"))

}