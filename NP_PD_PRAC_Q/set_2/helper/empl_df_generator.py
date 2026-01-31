"""
    Pandas (Intermediate)
    A DataFrame contains emp_id, department, quarter, and performance_score.
"""
"""
    emp_id          -> random_int
    dept            -> values from list
    quater          -> fixed values from list
    performance_scr -> random int from 1,5
"""

import pandas as pd
from faker import Faker
import random

fake = Faker()

def generator():
    # Settings
    num_employees = 50
    departments = ["HR", "IT", "Finance", "Marketing"]
    quarters = ["Q1", "Q2", "Q3", "Q4"]

    # Create empty lists for each column
    emp_ids = []
    depts = []
    quarter_list = []
    perf_scores = []

    for emp_id in range(1, num_employees + 1):
        dept = random.choice(departments)  # assign one dept per employee
        for quarter in quarters:
            emp_ids.append(emp_id)
            depts.append(dept)
            quarter_list.append(quarter)
            perf_scores.append(random.randint(1, 5))  # performance score 1-5

    # Create dictionary
    data_dict = {
        "emp_id": emp_ids,
        "department": depts,
        "quarter": quarter_list,
        "performance_score": perf_scores
    }

    # Convert to DataFrame
    df = pd.DataFrame(data_dict)
    return df

if __name__=="__main__":
    print(generator())

