from set_11_problem.file_processor import FileProcessor
from set_11_problem.jsonprocessor import JsonProcessor

if __name__=="__main__":

    json_processor = JsonProcessor()

    print(json_processor.validate("demo_json.json"))
    print(json_processor.extract("demo_json.json"))
    print(json_processor.summerize("demo_json.json"))

