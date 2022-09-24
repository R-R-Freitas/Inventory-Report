from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter

green = [
    "\033[32mData de fabricação mais antiga:\033[0m",
    "\033[32mData de validade mais próxima:\033[0m",
    "\033[32mEmpresa com mais produtos:\033[0m"
]

blue = [
    "\033[36m2020-09-06\033[0m",
    "\033[36m2023-09-17\033[0m"
]

red = [
    "\033[31mTarget Corporation\033[0m"
]

result = (f"{green[0]} {blue[0]}\n"
          f"{green[1]} {blue[1]}\n"
          f"{green[2]} {red[0]}")


def test_decorar_relatorio():
    csv_data = CsvImporter.import_data("inventory_report/data/inventory.csv")
    simple_report = ColoredReport(SimpleReport)
    colored_report = simple_report.generate(csv_data)
    assert colored_report == result
