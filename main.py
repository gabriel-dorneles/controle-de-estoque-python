import json
import unicodedata

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

def ler_texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor
        
        print("Esse campo não pode ficar vazio!")

def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor > 0:
                return valor

            print("Digite um número maior que zero!")

        except ValueError:
            print("Digite apenas números inteiros")      

def ler_inteiro_nao_negativo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor >= 0:
                return valor

            print("O valor não pode ser negativo!")

        except ValueError:
            print("Digite apenas números inteiros!")

def ler_preco(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)

            if valor >= 0:
                return valor

            print("O preço não pode ser negativo.")
        except ValueError:
            print("Digite um preço válido.")

def ler_texto_opcional(mensagem, valor_atual):
    valor = input(mensagem).strip()

    if valor == "":
        return valor_atual

    return valor

def ler_preco_opcional(mensagem, valor_atual):
    while True:
        entrada = input(mensagem).strip()

        if entrada == "":
            return valor_atual

        entrada = entrada.replace(",", ".")
        try:
            valor = float(entrada)

            if valor>= 0:
                return valor

            print("O preço não pode ser negativo!")

        except ValueError:
            print("Digite um preço válido ou pressione Enter para manter o valor atual.")

def normalizar_texto(texto):
    texto = texto.strip().casefold()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto

def cadastrar_produto():
    global proximo_codigo
    print("\n--- CADASTRO DE PRODUTO ---")
    codigo = proximo_codigo

    categoria = ler_texto_obrigatorio("Categoria: ")
    marca = ler_texto_obrigatorio("Marca: ")
    modelo = ler_texto_obrigatorio("Modelo: ")
    cor = ler_texto_obrigatorio("Cor: ")
    quantidade = ler_inteiro_nao_negativo("Quantidade: ")
    preco = ler_preco("Preço: R$ ")

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

    if len(produtos) == 0:
        print("\nNenhum produto cadastrado!")
        return

    print("1 - Buscar por código")
    print("2 - Buscar por categoria")
    print("3 - Buscar por marca")
    print("4 - Buscar por modelo")

    tipo_busca = input("\nEscolha uma opção: ")

    encontrados = []

    if tipo_busca == "1":
        codigo = ler_inteiro_positivo("Digite o código do produto: ")

        produto = buscar_por_codigo(codigo)

        if produto is not None:
            encontrados.append(produto)
                
    elif tipo_busca in ["2", "3", "4"]:

        if tipo_busca == "2":
            campo = "categoria"
            nome_campo = "categoria"

        elif tipo_busca == "3":
            campo = "marca"
            nome_campo = "marca"

        else:
            campo = "modelo"
            nome_campo = "modelo"

        termo = input(f"Digite a {nome_campo}: ").strip()

        if termo == "":
            print("\nA busca não pode ficar vazia.")
            return

        termo_normalizado = normalizar_texto(termo)

        for produto in produtos:
            valor_produto = normalizar_texto(produto[campo])

            if termo_normalizado in valor_produto:
                encontrados.append(produto)

    else:
        print("\nOpção inválida.")
        return

    if len(encontrados) == 0:
        print("\nNenhum produto encontrado.")
        return

    print(f"\n--- PRODUTOS ENCONTRADOS: {len(encontrados)} ---")

    for produto in encontrados:
        print("\n-------------------------------")
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
    codigo = ler_inteiro_positivo("Digite o código do produto: ")
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado!")
        return

    print(f"\nProduto: {produto['marca']} {produto['modelo']} - {produto['cor']}")
    print(f"Estoque atual: {produto['quantidade']}")
    quantidade = ler_inteiro_positivo("Quantidade de entrada: ")

    if quantidade <= 0:
        print("\nA quantidade deve ser maior que zero.")
        return

    produto["quantidade"] += quantidade
    salvar_produtos()
    print("\nEntrada realizada com sucesso!")
    print(f"Novo estoque: {produto['quantidade']}")

def saida_estoque():
    print("\n--- SAÍDA DE ESTOQUE ---")
    codigo = ler_inteiro_positivo("Digite o código do produto: ")
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado!")
        return

    print(f"\nProduto: {produto['marca']} {produto['modelo']} - {produto['cor']}")
    print(f"Estoque atual: {produto['quantidade']}")
    quantidade = ler_inteiro_positivo("Quantidade de saída: ")

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
    codigo = ler_inteiro_positivo("Digite o código do produto: ")
    produto = buscar_por_codigo(codigo)

    if produto is None:
        print("\nProduto não encontrado!")
        return
    
    print("\nPressione Enter para manter o valor atual")

    produto["categoria"] = ler_texto_opcional(
        f"Categoria [{produto['categoria']}]: ",
        produto["categoria"]
    )

    produto["marca"] = ler_texto_opcional(
        f"Marca [{produto['marca']}]: ",
        produto["marca"]
    )

    produto["modelo"] = ler_texto_opcional(
        f"Modelo [{produto['modelo']}]: ",
        produto["modelo"]
    )

    produto["cor"] = ler_texto_opcional(
        f"Cor [{produto['cor']}]: ",
        produto["cor"]
    )

    produto["preco"] = ler_preco_opcional(
        f"Preço [{produto['preco']:.2f}]: ",
        produto["preco"]
    )

    salvar_produtos()
    print("\nProduto atualizado com sucesso!")

def excluir_produto():
    print("\n--- EXCLUIR PRODUTO ---")
    codigo = ler_inteiro_positivo("Digite o código do produto: ")
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