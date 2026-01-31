"""
Task 6: Value Counts Pie Chart
Create a DataFrame with:
gender (Male/Female values)
Use value_counts().
Plot a pie chart showing gender distribution
"""
import matplotlib.pyplot as plt

from helper.generator import gender_df


def gender_count(data):

    group_by_gender_count = data["gender"].value_counts()
    return group_by_gender_count


if __name__=="__main__":
    sample_data = gender_df()
    print(f"SAMPLE DATA:\n{sample_data}")

    count_df = gender_count(sample_data)
    males = count_df["M"]
    females = count_df["F"]

    plt.pie([males,females], labels=["M","F"],autopct= "%1.1f%%")
    plt.show()