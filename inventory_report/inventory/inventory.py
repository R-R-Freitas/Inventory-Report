import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, report_type):
        with open(file, mode='r') as file_data:
            file_reader = csv.reader(file_data, delimiter=',', quotechar='"')
            header, *data = file_reader
            results = []
            for row in range(len(data)):
                line = {}
                for column in range(len(header)):
                    line[header[column]] = data[row][column]
                results.append(line)
            match report_type:
                case "simples": return(SimpleReport.generate(results))
                case "completo": return(CompleteReport.generate(results))
                case _: return()
