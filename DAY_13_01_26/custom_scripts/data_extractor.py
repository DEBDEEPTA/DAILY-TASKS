import pandas as pd
import os
import json

def csv_reader(csv_path, json_path, range_key, min_val, max_val):

    df = pd.read_csv(csv_path)
    filtered_df = df[df["battery"].between(min_val, max_val)]
    selected_fields = filtered_df[["vehicle_type", "vehicle_id"]]
    new_data = selected_fields.to_dict(orient = "records")


    if os.path.exists(json_path):
        with open(json_path, "r") as file:
            json_data = json.load(file)
    else:
        json_data = {}


    if range_key not in json_data:
            json_data[range_key] = []

    json_data[range_key].extend(new_data)
    with open(json_path, "w") as file:
        json.dump(json_data, file, indent=4)



if __name__ == "__main__":
    csv_path = "vehicle_data.csv"
    json_path = "vehicle_data.json"

    battery_ranges = {
        "0-10": (0, 10),
        "10-20": (10, 20),
        "20-30": (20, 30),
        "30-40": (30,40),
        "40-50": (40,50),
        "50-60": (50,60),
        "60-70": (60,70),
        "70-80":(70,80),
        "80-90":(80,90),
        "90-100":(90,100)
    }

    for range_key, (min_val, max_val) in battery_ranges.items():
        csv_reader(csv_path, json_path, range_key, min_val, max_val)


