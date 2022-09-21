import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, report_type):
        with open(file, mode="r") as file_data:
            file_reader = csv.reader(file_data, delimiter=",", quotechar='"')
            header, *data = file_reader
            results = []
            for row in range(len(data)):
                line = {}
                for column in range(len(header)):
                    line[header[column]] = data[row][column]
                results.append(line)
            if report_type == "simples":
                return SimpleReport.generate(results)
            else:
                return CompleteReport.generate(results)
