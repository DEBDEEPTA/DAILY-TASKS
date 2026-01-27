"""
Pandas (Intermediate)
A DataFrame contains student_id, course_id, login_date, and minutes_spent.
Task:
    Identify inactive students (no login in last 7 days)
    Calculate average session duration per course
    Find top 3 courses with the highest engagement
"""
from helper.generator import studnet_data_generator
import pandas as pd


def inactive_students(df):
    most_recent_date = df['login_date'].max()
    most_recent_seven_date = most_recent_date - pd.Timedelta(days=7)

    filter_mask = df['login_date'] < most_recent_seven_date
    filtered_df = df[filter_mask]

    filtered_student_df = filtered_df["student_id"].unique()

    return filtered_student_df


def avg_session_duration(df):
    course_mean_vals = df.groupby('course_id')['minutes_spent'].mean()
    return course_mean_vals


def top_three_courses(df):
    net_course_durations = df.groupby('course_id')['minutes_spent'].sum()

    top_three_crs = net_course_durations.sort_values(ascending=False).head(3)

    return top_three_crs


if __name__ == "__main__":
    sample_data = studnet_data_generator()
    print(f"SAMPLE DATA:\n{sample_data}")

    print(f"INACTIVE STUDENTS:\n{inactive_students(sample_data)}")

    print(f"AVG SESSION DURATION:\n{avg_session_duration(sample_data)}")

    print(f"TOP 3 COURSES:\n{top_three_courses(sample_data)}")

