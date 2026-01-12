from set_11_problem.file_processor import FileProcessor
import csv

class CsvProcessor(FileProcessor):

    def process(self,path):
        print("processing csv")

    def validate(self,path):
        print("Validating CSV")
        with open(path, newline='') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if headers is None:
                return False
            else:
                return True

    def extract(self, path):

        with open(path, newline='') as f:
            csv_dictionary =  list(csv.DictReader(f))
            return csv_dictionary


    def summerize(self,path):

        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            return rows