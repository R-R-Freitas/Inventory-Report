import xmltodict
import xml
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError("Arquivo inválido")
        try:
            with open(path, mode="r", encoding="utf-8") as file:
                return(xmltodict.parse(file.read())["dataset"]["record"])
        except (
            TypeError,
            xml.parsers.expat.ExpatError,
        ):
            raise ValueError("Arquivo inválido")
