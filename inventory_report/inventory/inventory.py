import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, mode="r") as file:
            if path.endswith(".csv"):
                file_reader = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = file_reader
                results = cls.csv_to_dict(header, data)
                return cls.call_generate_report(results, report_type)
            elif path.endswith(".json"):
                with open(path) as file:
                    results = json.load(file)
                return cls.call_generate_report(results, report_type)
            elif path.endswith(".xml"):
                with open(path, mode="r", encoding="utf-8") as file:
                    results = xmltodict.parse(file.read())["dataset"]["record"]
                return cls.call_generate_report(results, report_type)

    @classmethod
    def call_generate_report(cls, results, report_type):
        if report_type == "simples":
            return SimpleReport.generate(results)
        else:
            return CompleteReport.generate(results)

    @classmethod
    def csv_to_dict(cls, header, data):
        results = []
        for row in range(len(data)):
            line = {}
            for column in range(len(header)):
                line[header[column]] = data[row][column]
            results.append(line)
        return results
