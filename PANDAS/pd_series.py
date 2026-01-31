from copyreg import constructor

import pandas as pd

# CREATING A SERIES
# SERIES -> INDEX_VALUE : VALUE
#           dtype: ..

def pd_series():
    series_data = pd.Series(
        [1, 2, 3,None,5],
        index=["a", "b", "c", "d", "e"], # OPTIONAL
        # if Index is not Given It will take default index starting from 0 at each row incremented by 1
        dtype= "Int64"  # OPTIONAL IF NOT MENTIONED dtype WILL BE AS PER THE DATA/VALUE

        # nulablility support dtypes
        #  -> Int64
        #  -> float (float64)
        #  -> Float64
        #   ................


    )
    return series_data

def pd_series_without_index():
    series_data = pd.Series(
        ["a","b","c","d","e"],
                             # index given automatically
                             # dtype decided by py_interpreter BASED ON VALUE DTYPE
    )
    return series_data


def pd_partial_indexing():
    series_data = pd.Series(
        [1,2,4.0,3,2],
        index=["a","b","c"]   # Raises ValueError
                          # len(index) == len(data) strictly
    )
    return  series_data

def ped_partial_reindexing():
    series_data = pd.Series(
        [1,2,3,4],
        index=["a","b","c","d"]
    )
    new_series_data = series_data.reindex(["a","b","c","d","e"])
    # # note -> reindex doesn't modify the original series data
    #         -> _________FOR MISSING VALUE____________________
    #             key: NaN
    #         ->__________LESS KEYS THAN ORIGINAL SERIES_______
    #             truncate series as per the number of keys
    return  new_series_data

def full_series_constructor():
    # DEFAULT SERIES CONSTRUCTOR
    series_data = pd.Series(data= None,index = None,name = None,copy= False)
    # ASSIGNING KEY : VALUE PAIR ONCE AT A TIME
    series_data["a"] = 1
    series_data["b"] = 2
    # RE-ASSIGNING dtype AFTER CREATION
    series_data = series_data.astype("Int64")   # USE .astype() Function
    return series_data

if __name__=="__main__":
    pd_series()
    pd_series_without_index()
    #print(pd_partial_indexing()) # Raises ValueError
                                   # len(index) == len(data) strictly

    print(ped_partial_reindexing())
    print(full_series_constructor())


