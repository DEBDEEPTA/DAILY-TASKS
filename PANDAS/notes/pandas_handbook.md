
## PANDAS
Pandas is a data manipulation and analysis library built on top of NumPy.
It is designed to work with structured data (tabular, labeled, heterogeneous data).
 ```
 pip install pandas
 ```
| Structure | Description           |
| --------- | --------------------- |
| Series    | 1-D labeled array     |
| DataFrame | 2-D labeled table     |
| Index     | Immutable axis labels |

### SERIES
1.  _SERIES ATTRIBUTES_
    
    | Attribute | Meaning                |
    | --------- | ---------------------- |
    | s.values  | Underlying NumPy array |
    | s.index   | Index labels           |
    | s.dtype   | Data type              |
    | s.size    | Number of elements     |
    | s.shape   | Dimension              |
    | s.ndim    | Number of dimensions   |
2. _SERIES METHODS_
    
    | Method         | Purpose                                    |
    | -------------- |--------------------------------------------|
    | head()         | First n rows                               |
    | tail()         | Last n rows                                |
    | sum()          | Sum                                        |
    | mean()         | Mean                                       |
    | min(), max()   | Min / Max                                  |
    | value_counts() | Frequency of each unique values            |
    | apply()        | Apply custom function flitaration (lambda) |
    | isnull()       | Missing values                             |
    | fillna()       | Replace NaN                                |


