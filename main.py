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

while True:
    print("\n==============================")
    print("      CONTROLE DE ESTOQUE")
    print("==============================")

    print("1 - Cadastrar produto")
    print("2 Listar produtos")
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

    elif opcao == "0":
        print("\n Sistema encerrado.")
        break
    else:
        print("\nOpção ainda não implementada.")