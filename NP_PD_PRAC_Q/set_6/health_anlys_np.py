"""
NumPy (Intermediate)
Patient vitals (heart rate) are stored for 60 patients over 24 hours in a NumPy array.
Task:
    Compute hourly average heart rate
    Detect abnormal readings outside the normal range
    Replace missing values using forward fill logic
"""

"""
    logic ->
        [   # 24 values each representing hertz
            [89,90,23....] <- p1
            [] <- p2
            .
            .
            [] <- p60
        ] 
        
        size -> (60,24)
"""
import numpy as np

def hrs_avg_heart_rate(data):

    hrs_avg_rate = data.mean(axis=0)
    return hrs_avg_rate

def outliers_heart_rates(data, min_val = 60, max_val = 100):

    filter_mask = (data < min_val) | (data > max_val)
    outliers_data = data[filter_mask]
    return outliers_data

def forward_fill_vals(data):

    data_copy = data
    paitents, hrs = data.shape
    for p in range(paitents):
        for h in range(hrs):
            if np.isnan(data_copy[p,h]):
                data_copy[p,h] = data_copy[p,h-1] # fill with previous valid hour

    return data_copy

if __name__=="__main__":
    # Normal human heart rate range 60-100bpm
    # considered min -> 20bpm     # to represent abnormality
    # considered max -> 150bpm    # to represent abnormality

    data = np.random.randint(20,150,(60,24))
    data = data.astype(float) # Convert data to float so

    # SETTING SAMPLE MISSING DATA
    data[2][3] = np.nan
    data [12][1] = np.nan
    data [12][4] = np.nan
    data[32][3] = np.nan
    data[56][22] = np.nan


    print(f"SAMPLE DATA:\n{data}")

    print(f"Avg heart rate / hrs :\n{hrs_avg_heart_rate(data)}")

    print(f"Abnormal Readings:\n{outliers_heart_rates(data)}")

    print(f"DATA AFTER CLEANING USING FORWARD FILL:\n{forward_fill_vals(data)}")