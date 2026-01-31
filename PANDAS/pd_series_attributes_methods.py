import pandas as pd
def series_atributes():
    series_data = pd.Series(
        [1,2,3,4,5,6,7],
        ["a","b","c","d","e","f","g"],
        "Float64",
        "Numbers",
    )
    print("___________VALUES___________")
    print(f"values : {series_data.values}")

    print("___________INDEXES___________")
    print(f"Indexes: {series_data.index}")

    print("__________DTYPE_____________")
    print(f"dtype: {series_data.dtype}")

    print("____________SIZE___________")
    print(f"size: {series_data.size}")
    print("____________SHAPE___________")
    print(f"shape: {series_data.shape}")
    print("____________NDIM___________")
    print(f"ndim: {series_data.ndim}")


def pd_series_methods():
    series_data = pd.Series([10,20,30,40,50,60,70,80],
                            ["A","B","C","D","E","F","G","H"])

    print(f"sum: {series_data.sum()}")
    print(f"min: {series_data.min()}")
    print(f"max: {series_data.max()}")


    print("________FIRST_N_ROWS_______")
    print("DEFAULT RETURNS FIRST 5 ROWS")
    print(series_data.head())  # DEFAULT RETURNS FIRST 5 ROWS
    print("RETURNING FIRST 3 ROWS")
    print(series_data.head(3))


if __name__=="__main__":
    #series_atributes()
    pd_series_methods()