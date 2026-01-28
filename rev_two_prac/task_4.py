"""
Create a DataFrame with:
marks (50 random values between 0 and 100)
Plot a histogram with appropriate bins.
"""
from helper.generator import marks_df
from matplotlib import pyplot as plt


if __name__=="__main__":
    sample_data = marks_df()
    print(f"SAMPLE DATA:\n{sample_data}")

    marks = sample_data.values

    plt.hist(marks)
    plt.show()

