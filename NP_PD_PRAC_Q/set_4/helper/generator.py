from datetime import date

from faker import Faker
import pandas as pd
def studnet_data_generator():
    """ A DataFrame contains student_id, course_id, login_date, and minutes_spent."""
    fk = Faker()

    student_id_list = list(range(1,51)) # 50 UNIQUE STUDENT ID
    course_id_list = ["C1","C2","C3","C4","C5"]

    start = date(2021, 1, 1)
    end = date(2025, 12, 31)

    max_time = 6*60
    min_time = 1*60
    student_id = []
    course_id = []
    login_date = []
    minutes_spent = []


    data = {
        "student_id": student_id,
        "course_id":course_id,
        "login_date": login_date,
        "minutes_spent":minutes_spent,
    }

    for _ in range(151): # total 151 records
        student_id.append(fk.random_element(student_id_list))
        course_id.append(fk.random_element(course_id_list))
        login_date.append(fk.date_between_dates(start,end))
        minutes_spent.append(fk.random_int(min_time,max_time+1))

    return  pd.DataFrame(data)

if __name__=="__main__":
    print(studnet_data_generator().head())
