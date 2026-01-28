"""
Task 5: Scatter Plot
Create a DataFrame with:
hours_studied
score
Plot a scatter plot.
Identify if there is a positive correlation visually.
"""
from helper.generator import study_df
from matplotlib import pyplot as plt


if __name__=="__main__":
    sample_data =study_df()
    print(f"SAMPLE DATA:\n{sample_data}")

    hrs_study = sample_data["hour_studies"].values
    scores = sample_data["scores"].values

    plt.xlabel("Hours")
    plt.ylabel("Scores")
    plt.grid(visible=True)
    plt.scatter(hrs_study,scores)
    plt.show()