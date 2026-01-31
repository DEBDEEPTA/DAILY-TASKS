"""
Task 1: Basic Line Plot
Create a DataFrame with columns:
day → 1 to 7
sales → random integers between 100 and 500
Plot a line chart showing sales trend across days.
"""
import pandas as pd
from matplotlib import pyplot as plt
from helper.generator import sales_data_generator

if __name__=="__main__":
    sample_data = sales_data_generator()
    print(f"SAMPLE _DATA:\n{sample_data}")

    net_sale_per_day = sample_data.groupby("days")["sales"].sum()

    # TEST CHECKPOINT
    #print(net_sale_per_day)

    plt.xlabel("Days")
    plt.ylabel("Sales")

    plt.title("Sales Data")
    plt.plot(net_sale_per_day)
    plt.show()