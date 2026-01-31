"""
You are given a DataFrame containing order_id, customer_id, order_date, and order_amount.
Task:
    Convert order_date to datetime
    Find the monthly total revenue
    Identify the month with the highest number of unique customers
"""
import pandas as pd

def order_analysis(orders_df):
    #Convert order_date to datetime (Renaming Column)
    orders_df = orders_df.rename(columns = {"order_date":"datetime"})
    # Type casting datetime column str ---> datetime

    orders_df["datetime"] = pd.to_datetime(orders_df["datetime"])

    # print(type(orders_df["datetime"][0])) # To Check if str ---> datetime

    """ FINDING MONTHLY TOTAL REVENUE
        -> ADD MONTH COLUMN
        -> GROUP RECORDS BY MONTH
        -> SELECT ORDER_AMOUNT WHILE GROUPING
        -> USE SUM TO CALCULATE SUM OF ORDER_AMOUNT ALL FOR EACH FROUP
    """
    #adding month column to table

    orders_df["month"] = orders_df["datetime"].dt.to_period("M")

    monthly_orders_sum = orders_df.groupby("month")["order_amount"].sum()

    """IDENTIFYING MONTH WITH HIGHEST NUMBER OF UNIQUE_CUSTOMERS
        -> GROUP BY MONTH
        -> SELECT CUSTOMER_ID WHILE GROUPING
        -> USE nunique() to EXTRACT UNIQUE VALUES FROM A COLUMN 
        -> use idmax() to get label(month) for the maximum unique customers
        
        (note)
            -> argmax(), argmin() will return the index -> 0,1,2 ....
            -> idmax(), idmin() will return the label name
    """

    # EXTRACTING UNIQUE CUSTOMERS PER MONTH
    monthly_unique_customers = orders_df.groupby("month")["customer_id"].nunique() # note -> monthly_unique_customers is a series


    # EXTRACTING THE LABEL/INDEX/MONTH FOR THE MAXIMUM NUMBER OF UNIQUE CUSTOMERS
    month_with_max_unique_customers = monthly_unique_customers.idxmax()

    print(f"Modified Order DF :\n{orders_df}")
    print(f"Monthly Total Revenue:\n{monthly_orders_sum}")
    print(f"Month with max unique Customers: \n{month_with_max_unique_customers}")
    

if __name__=="__main__":
    # GENERATED SAMPLE DATA
    data = {
        "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                     111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

        "customer_id": ["C001", "C002", "C003", "C001", "C004", "C002", "C005", "C006", "C003", "C007",
                        "C001", "C008", "C004", "C009", "C010", "C002", "C006", "C011", "C003", "C012"],

        "order_date": ["2025-01-05", "2025-01-08", "2025-01-15", "2025-01-28", "2025-02-03",
                       "2025-02-10", "2025-02-14", "2025-02-22", "2025-03-01", "2025-03-05",
                       "2025-03-12", "2025-03-18", "2025-03-25", "2025-04-02", "2025-04-09",
                       "2025-04-15", "2025-04-21", "2025-05-03", "2025-05-10", "2025-05-19"],

        "order_amount": [1200, 800, 1500, 600, 2000,
                         950, 1300, 1100, 1700, 900,
                         1250, 1600, 1400, 2100, 1800,
                         1000, 1500, 2200, 1350, 1900]
    }

    orders_df = pd.DataFrame(data=data)

    order_analysis(orders_df)