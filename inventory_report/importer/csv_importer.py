import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.csv'):
            raise ValueError("Arquivo inválido")
        try:
            with open(path, mode="r") as file:
                file_reader = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = file_reader
                return cls.csv_to_dict(header, data)
        except (TypeError):
            raise ValueError("Arquivo inválido")

    @classmethod
    def csv_to_dict(cls, header, data):
        results = []
        for row in range(len(data)):
            line = {}
            for column in range(len(header)):
                line[header[column]] = data[row][column]
            results.append(line)
        return results
