import json

from DAY_12_01_26.set_11_problem.file_processor import FileProcessor

class JsonProcessor(FileProcessor):

    def process(self,path):
        print("processing json")

    def validate(self,path):
        print("Validating Json")
        with open(path, "r") as f:
            data = json.load(f) # Reading Json

            if(isinstance(data, dict)):
                return True
            else:
                return False

    def extract(self,path):
        print("json data")
        with open(path, "r") as file_obj:
            data = json.load(file_obj)

            return  data

    def summerize(self,path):
        with open(path, "r") as file_obj:
            data = json.load(file_obj)

            constraints = data.get("constraints")

            words = constraints.split()
            words_count = len(words)
            print("json summerize")
            return words_count

