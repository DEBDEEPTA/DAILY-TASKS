"""
NumPy (Intermediate)
Stock prices of 10 companies over 90 trading days are stored in a NumPy array.
Task:
    Calculate daily returns
    Compute volatility (standard deviation) per stock
    Identify the stock with the highest risk
"""
"""
    logic ->
        [   # stock price of company 1,2,3....10
            [sp1,sp2,sp3 ...] <- d1
            [] <- d2
            [] <- d3
             .
             .
            [] <- d90
        ]
        (90,10)
"""
import numpy as np

if __name__ == "__main__":
    # consider min stock price 10000
    # consider max stock price 100000
    min_price = 10000
    max_price = 100000
    sample_data = np.random.randint(min_price,max_price, (90,10))

    print(f"SAMPALE_DATA:\n{sample_data}")