"""
Set 3 (Weather Monitoring System)
    NumPy (Intermediate)
        A weather station stores hourly temperature readings for 7 days in a NumPy array of shape (7, 24).
    Task:
        Find the daily maximum and minimum temperature
        Identify the day with the largest temperature variation
        Replace outliers beyond ±2 standard deviations with the mean temperature
"""
import random
from random import Random as rnd

import numpy as np

def daily_max_temp(data):

    daily_max_temp = data.max(axis=1)
    return  daily_max_temp

def largest_temp_var(data):
    """

    """

    max_temps_of_days = data.max(axis=1)
    min_temps_of_days = data.min(axis=1)

    temp_variance_of_days = max_temps_of_days - min_temps_of_days

    max_temp_variance = temp_variance_of_days.argmax()
    return max_temp_variance

def normalize_outliers(data):
    mean_temp = data.mean()
    std_val = data.std()

    low_limit = mean_temp - (std_val*2)
    up_limit = mean_temp + (std_val*2)

    data = np.where((data < low_limit) | (data > up_limit), mean_temp, data)

    return data

if __name__ == "__main__":
    # CONSIDERING MAX TEMP => 67
    # CONSIDERING MIN TEMP => -2

    temp_data = np.random.randint(-2,68,(7,24))

    print(daily_max_temp(temp_data))
    print(largest_temp_var(temp_data))
    print(normalize_outliers(temp_data))