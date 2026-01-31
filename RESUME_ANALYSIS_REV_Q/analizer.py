from typing import DefaultDict

from resume_text_analizer.helpers.file_reader import file_reader
from resume_text_analizer.helpers.matchers import get_email, get_phone, get_name, get_collage, get_skills

"""
    Problem 3: Resume Text Analyzer
    You are building a resume screening tool that processes uploaded text resumes.
     The resumes come in different formats and writing styles.
    Your task is to:
    Extract key information from unstructured text
    
    Identify repeated sections and remove redundancy
    
    Detect malformed sections using regex patterns
    
    Organize extracted data into structured containers
    
    The design should allow new extraction rules to be added without modifying existing logic and must be fully unit tested.
"""
def default_value():
    return "Invalid key"

def extracted_data(file_path):
    file_reader_data_list = file_reader(file_path)

    dict_val = DefaultDict(default_value)

    dict_val["name"] = get_name(file_reader_data_list).strip()
    dict_val["email"] = get_email(file_reader_data_list).strip()
    dict_val["phone"] = get_phone(file_reader_data_list).strip()
    dict_val["collage"] = get_collage(file_reader_data_list).strip()
    dict_val["skills"] = get_skills(file_reader_data_list).strip()

    return dict_val

if __name__=="__main__":
    file_path = "resumes/sample.txt"

    file_reader_data_list = file_reader(file_path)

    dict_val = extracted_data(file_path)
    for k,v in dict_val.items()set_7
set_4
set_6
set_5:
        print(f"{k} -> {v}")
