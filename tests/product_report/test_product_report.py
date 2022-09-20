from inventory_report.inventory.product import Product

id = 1
nome_do_produto = "Frágil"
nome_da_empresa = "Fabricante"
data_de_fabricacao = "2022-05-11"
data_de_validade = "2023-05-11"
numero_de_serie = "A01B02"
instrucoes_de_armazenamento = "Com muito cuidado!"
sentence = (f"O produto {nome_do_produto} fabricado em {data_de_fabricacao} "
            f"por {nome_da_empresa} com validade até {data_de_validade} "
            f"precisa ser armazenado {instrucoes_de_armazenamento}.")


def create_product_mock():
    return Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )


def test_relatorio_produto():
    product = create_product_mock()
    assert str(repr(product)) == sentence
