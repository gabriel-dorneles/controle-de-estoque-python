produtos = []

def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")

    codigo = len(produtos) + 1

    categoria = input("Categoria: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))

    produto = {
        "codigo": codigo,
        "categoria": categoria,
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")
    print(f"Código do Produto: {codigo}")

def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("\n----------------------------")
        print(f"Código: {produto['codigo']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Marca: {produto['marca']}")
        print(f"Modelo: {produto['modelo']}")
        print(f"Cor: {produto['cor']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")

def buscar_produto():
    print("\n--- BUSCAR PRODUTO ---")
    print("1 - Buscar por código")
    print("2 - Buscar por categoria")
    print("3 - Buscar por marca")
    print("4 - Buscar por modelo")

    tipo_busca = input("\nEscolha uma opção: ")

    encontrados = []

    if tipo_busca == "1":
        codigo = int(input("Digite o código do produto: "))

        for produto in produtos:
            if produto["codigo"] == codigo:
                encontrados.append(produto)
                
    elif tipo_busca == "2":
        categoria = input("Digite a categoria do produto: ").lower()

        for produto in produtos:
            if produto["categoria"].lower() == categoria:
                encontrados.append(produto)

    elif tipo_busca == "3":
        marca = input("Digite a marca do produto: ").lower()

        for produto in produtos:
            if produto["marca"].lower() == marca:
                encontrados.append(produto)

    elif tipo_busca == "4":
        modelo = input("Digite o modelo: ").lower()

        for produto in produtos:
            if produto["modelo"].lower() == modelo:
                encontrados.append(produto)

    else:
        print("Opção inválida!")
        return

    if len(encontrados) == 0:
        print("\nNenhum produto encontrado.")
        return

    print("\n--- PRODUTOS ENCONTRADOS ---")

    for produto in encontrados:
        print ("\n----------------------------------")
        print(f"Código: {produto['codigo']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Marca: {produto['marca']}")
        print(f"Modelo: {produto['modelo']}")
        print(f"Cor: {produto['cor']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")

while True:
    print("\n==============================")
    print("      CONTROLE DE ESTOQUE")
    print("==============================")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Entrada de estoque")
    print("5 - Saída de estoque")
    print("6 - Editar produto")
    print("7 - Excluir produto")
    print("8 - Relatório do estoque")
    print("0 - Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "0":
        print("\n Sistema encerrado.")
        break
    else:
        print("\nOpção ainda não implementada.")