"""
Task 2: Missing Values Bar Plot
Create a DataFrame with:
name
age (include some NaN values)
Fill missing ages with the mean.
Plot a bar chart of name vs age.
"""
import numpy as np
import pandas as pd
from helper.generator import name_age_df
from matplotlib import pyplot as plt

def data_filteration(data):
    mean_age = data["age"].mean()

    condition = (np.isnan(data["age"]) == False)

    filter_data = data.where(condition, mean_age)
    return filter_data


if __name__=="__main__":
    sample_data = name_age_df()
    print(f"SAMPLE DATA:\n{sample_data}")
    filtered_data = data_filteration(sample_data)
    print(f"FILTERED DATA:\n{filtered_data}")

    plt.xlabel("names")
    plt.ylabel("ages")

    names_numpy_arr = filtered_data.index.index.to_numpy()
    ages_numpy_arr = filtered_data.values
    plt.bar(names_numpy_arr,ages_numpy_arr)
    plt.show()




