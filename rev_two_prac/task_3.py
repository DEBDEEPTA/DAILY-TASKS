"""
Task 3: GroupBy + Bar Chart
Create a DataFrame with:
department
salary
Calculate average salary per department.
Visualize using a bar chart.
"""
from helper.generator import dept_sal_df
from matplotlib import pyplot as plt

def avg_sal_per_dept(data):

    group_by_avg_sal_per_dept = data.groupby("department")["salary"].mean()
    return group_by_avg_sal_per_dept

if __name__=="__main__":
    sample_data = dept_sal_df()
    print(f"SAMPLE DATA:\n{sample_data}")
    avg_sal_dept = avg_sal_per_dept(sample_data)
    print(f"AVERAGE SALARY PER DEPARTMENT:\n{avg_sal_dept}")


    avg_sal_numpy_lables = avg_sal_dept.index.to_numpy()
    avg_sal_numpy_arr_values = avg_sal_dept.to_numpy()

    plt.xlabel("Department")
    plt.ylabel("Average Salary")

    plt.bar(avg_sal_numpy_lables, avg_sal_numpy_arr_values)
    plt.show()