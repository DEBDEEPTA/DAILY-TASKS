
def file_reader(file_path):
    with open(file_path, "r") as file_obj:
        reader_data = file_obj.readlines()
        return reader_data