from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products=products)
        count_companies = super().count_product_per_company(products=products)
        print(count_companies)
        complete_report = ""
        for key, value in count_companies.items():
            complete_report += f"- {key}: {value}\n"
        return(
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{complete_report}"
        )
