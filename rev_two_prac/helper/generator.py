import pandas as pd
from faker import Faker
import numpy as np
def sales_data_generator():
    fk = Faker()
    days = []
    sales = []

    data = {
        "days":days,
        "sales":sales
    }

    # CONSIDERING 131 RECORDS
    for _ in range (131):
        days.append(fk.random_int(1,7))
        sales.append(fk.random_int(100,500))

    return pd.DataFrame(data)

def name_age_df():
    fk = Faker()
    name = []
    age = []

    data = {
        "name":name,
        "age": age,
    }

    # CONSIDERING 50 RECORDS
    for i in range(50):
        name.append(fk.first_name())
        if (i%2 == 0):
            age.append(np.nan)
        else:
            age.append(fk.random_int(18,65))

    return pd.DataFrame(data)


def dept_sal_df():
    fk = Faker()
    dept_list = ["IT","SALES","MNG","RND"]

    dept = []
    sal = []

    data = {
        "department":dept,
        "salary":sal,
    }

    #CONSIDERING 131 RECORDS
    for _ in range(131):
        dept.append(fk.random_element(dept_list))
        # CONSIDERING SALARY RANGE IN 25000 to 75000
        sal.append(fk.random_int(25000,75000))

    return pd.DataFrame(data)


def marks_df():
    fk = Faker()
    subs_list = ["PHYC","CHEM","MATH"]

    subs = []
    marks = []
    data = {
        "subjects": subs,
        "marks": marks
    }

    for _ in range(50):
        subs.append(fk.random_element(subs_list))
        marks.append(fk.random_int(0,100))

    return pd.DataFrame(data)


def study_df():
    fk = Faker()
    hour_studies = []
    scores = []
    data = {
        "hour_studies":hour_studies,
        "scores":scores
    }

    for _ in range(131):
        random_hrs = fk.random_int(0,6)
        hour_studies.append(random_hrs)
        # CONSIDERING SCORE RANGE OUT OF 5
        # BUILDING POSITIVE RELATIONSHIP W.R.T HOURS SPEND vs SCORES
        if(random_hrs == 0):
            scores.append(0.0)

        elif (random_hrs == 1):
            scores.append(2.0)

        elif (random_hrs == 2):
            scores.append(3.0)

        elif (random_hrs == 3):
            scores.append(3.5)

        elif (random_hrs == 4):
            scores.append(4.0)

        elif (random_hrs == 5):
            scores.append(4.5)

        elif(random_hrs == 6):
            scores.append(5.0)

    return pd.DataFrame(data)

def gender_df():
    fk = Faker()

    gender_list = ["F", "M"]

    name =   []
    gender = []

    data = {
        "name":name,
        "gender":gender
    }

    for i in range(131):
        name.append(fk.name())
        gender.append(fk.random_element(gender_list))

    return pd.DataFrame(data)

if __name__=="__main__":

    # print(name_age_df().head(10))
    # print(dept_sal_df().head(10))
    # print(marks_df().head(10))
    #print(study_df().head(10))
    print(gender_df().head(10))
