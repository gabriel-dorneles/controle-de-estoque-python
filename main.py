import json

ARQUIVO = "produtos.json"

def carregar_produtos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

def salvar_produtos():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


produtos = carregar_produtos()
if len(produtos) > 0:
    proximo_codigo = max(produto["codigo"] for produto in produtos) + 1
else:
    proximo_codigo = 1

def cadastrar_produto():
    global proximo_codigo
    print("\n--- CADASTRO DE PRODUTO ---")
    codigo = proximo_codigo

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
    proximo_codigo += 1
    salvar_produtos()

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


def buscar_por_codigo(codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

def entrada_estoque():
    print("\n--- ENTRADA DE ESTOQUE ---")
    codigo = int(input("Digite o código do produto: "))
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado!")
        return

    print(f"\nProduto: {produto['marca']} {produto['modelo']} - {produto['cor']}")
    print(f"Estoque atual: {produto['quantidade']}")
    quantidade = int(input("Quantidade de entrada: "))

    if quantidade <= 0:
        print("\nA quantidade deve ser maior que zero.")
        return

    produto["quantidade"] += quantidade
    salvar_produtos()
    print("\nEntrada realizada com sucesso!")
    print(f"Novo estoque: {produto['quantidade']}")

def saida_estoque():
    print("\n--- SAÍDA DE ESTOQUE ---")
    codigo = int(input("Digite o código do produto: "))
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado!")
        return

    print(f"\nProduto: {produto['marca']} {produto['modelo']} - {produto['cor']}")
    print(f"Estoque atual: {produto['quantidade']}")
    quantidade = int(input("Quantidade de saída: "))

    if quantidade <= 0:
        print("\nA quantidade deve ser maior que zero.")
        return

    if quantidade > produto["quantidade"]:
        print("\nEstoque insuficiente!")
        return

    produto["quantidade"] -= quantidade
    salvar_produtos()
    print("\nSaída realizada com sucesso!")
    print(f"Novo estoque: {produto['quantidade']}")

def editar_produto():
    print("\n--- EDITAR PRODUTO ---")
    codigo = int(input("Digite o código do produto: "))
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado!")
        return
    
    print("\nDeixe em branco o campo que não deseja alterar")

    categoria = input(f"Categoria [{produto['categoria']}]: ")
    marca = input(f"Marca [{produto['marca']}]: ")
    modelo = input(f"Modelo [{produto['modelo']}]: ")
    cor = input(f"Cor [{produto['cor']}]: ")
    preco = input(f"Preço [{produto['preco']:.2f}]: ")

    if categoria != "":
        produto["categoria"] = categoria

    if marca != "":
        produto["marca"] = marca

    if modelo != "":
        produto["modelo"] = modelo

    if cor != "":
        produto["cor"] = cor

    if preco != "":
        produto["preco"] = float(preco)

    salvar_produtos()
    print("\nProduto atualizado com sucesso!")

def excluir_produto():
    print("\n--- EXCLUIR PRODUTO ---")
    codigo = int(input("Digite o código do produto: "))
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    print(f"\nProduto: {produto['marca']} {produto['modelo']} - {produto['cor']}")

    while True:
        confirmacao = input("Deseja realmente excluir este produto? (s/n): ").lower()

        if confirmacao == "s":
            produtos.remove(produto)
            salvar_produtos()
            print("\nProduto excluído com sucesso!")
            break

        elif confirmacao == "n":
            print("\nExclusão cancelada.")
            break

        else:
            print("\nOpção inválida. Digite apenas 's' ou 'n'.")

def relatorio_estoque():
    print("\n========== RELATÓRIO DO ESTOQUE ==========")

    if len(produtos) == 0:
        pront("\nNenhum produto cadastrado!")
        return

    total_unidades = 0
    valor_total = 0
    categorias = {}

    for produto in produtos:
        total_unidades += produto["quantidade"]
        valor_produto = produto["quantidade"] * produto["preco"]
        valor_total += valor_produto
        categoria = produto ["categoria"]

        if categoria in categorias:
            categorias[categoria] += produto["quantidade"]
        else:
            categorias[categoria] = produto["quantidade"]

    print(f"\nProdutos cadastrados: {len(produtos)}")
    print(f"Total de unidades: {total_unidades}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    print("\n--- UNIDADES POR CATEGORIA ---")

    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade}")

    print("\n--- ESTOQUE BAIXO ---")

    encontrou_estoque_baixo = False

    for produto in produtos:
        if produto["quantidade"] <=2:
            print(
                f"Código {produto['codigo']} | "
                f"{produto['marca']} {produto['modelo']} | "
                f"Quantidade: {produto['quantidade']}"
            )
            encontrou_estoque_baixo = True
    if encontrou_estoque_baixo == False:
        print("Nenhum produto com estoque baixo.")






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

    elif opcao == "4":
        entrada_estoque()

    elif opcao == "5":
        saida_estoque()
    
    elif opcao == "6":
        editar_produto()

    elif opcao == "7":
        excluir_produto()

    elif opcao == "8":
        relatorio_estoque()

    elif opcao == "0":
        print("\n Sistema encerrado.")
        break
    else:
        print("\nOpção ainda não implementada.")