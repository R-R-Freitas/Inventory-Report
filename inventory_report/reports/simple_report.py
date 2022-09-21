from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in products]
        )
        closest_date = min(
            [
                product["data_de_validade"]
                for product in products
                if product["data_de_validade"] > str(datetime.today().date())
            ]
        )
        company_with_most_products = cls.get_company_most_products(products)
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )

    @classmethod
    def count_product_per_company(cls, products):
        companies = dict()
        for product in products:
            if product["nome_da_empresa"] in companies.keys():
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1
        return companies

    @classmethod
    def get_company_most_products(cls, products):
        companies = cls.count_product_per_company(products)
        # source: https://stackoverflow.com/questions/268272/
        # getting-key-with-maximum-value-in-dictionary
        return max(companies, key=companies.get)
