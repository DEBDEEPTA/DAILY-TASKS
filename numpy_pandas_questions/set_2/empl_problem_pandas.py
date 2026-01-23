"""
Pandas (Intermediate)
A DataFrame contains emp_id, department, quarter, and performance_score.
Task:
    Group data by department
    Compute the quarter-wise average performance per department
    Identify departments showing consistent improvement across quarters
"""
from helper.empl_df_generator import generator

def empl_data_anlysis(df):
    #df_groupd_by_dept = df.groupby("department")
    """
        note ->
        1️⃣ Current code
            df_grouped_by_dept = df.groupby("department")
            print(df_grouped_by_dept)
            Output:
            <pandas.core.groupby.generic.DataFrameGroupBy object at 0x...
            ❌ This is why you see the memory address.
            2️⃣ What you need to do
            You need to aggregate after grouping. Common aggregations:
            .mean() → average
            .sum() → sum
            .count() → count of rows
            .size() → number of rows per group
    """
    qt_wise_avg_per_dept = df.groupby(["department","quarter"])["performance_score"].mean().unstack()
    """ FOR GROUPING W.R.T MULTIPLE LABELS PASS THE LABELS AS LIST"""

    """
        stack() vs unstack() in pandas
    """

    print(f"EMPLOYEE DATA GROUP BY DEPARTMENT:\n{qt_wise_avg_per_dept}")




if __name__=="__main__":
    sample_df = generator()
    print(f"SAMPLE DATASET:\n{sample_df}")

    empl_data_anlysis(sample_df)


