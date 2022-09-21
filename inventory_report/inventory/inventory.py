import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, mode="r") as file:
            if path.endswith(".csv"):
                file_reader = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = file_reader
                results = []
                for row in range(len(data)):
                    line = {}
                    for column in range(len(header)):
                        line[header[column]] = data[row][column]
                    results.append(line)
                return(cls.call_generate_report(results, report_type))
            elif path.endswith(".json"):
                with open(path) as file:
                    results = json.load(file)
                return(cls.call_generate_report(results, report_type))

    @classmethod
    def call_generate_report(cls, results, report_type):
        if report_type == "simples":
            return SimpleReport.generate(results)
        else:
            return CompleteReport.generate(results)
