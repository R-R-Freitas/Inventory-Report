from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = "Produto frágil"
    nome_da_empresa = "Fabricante"
    data_de_fabricacao = "2022-05-11"
    data_de_validade = "2023-05-11"
    numero_de_serie = "A01B02"
    instrucoes_de_armazenamento = "Com muito cuidado!"
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )
    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
