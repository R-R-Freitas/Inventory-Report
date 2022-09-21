import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.json'):
            raise ValueError("Arquivo inválido")
        try:
            with open(path) as file:
                return(json.load(file))
        except (TypeError, json.JSONDecodeError):
            raise ValueError("Arquivo inválido")
